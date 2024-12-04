#Python script that reads from a .json file with pointers and string locations and modifies the strings where they're supposed to be n the executable



"""
We have a JSON with the original japanese string positions, the japanese string, and our english translation. Example:
{
        "Location": "82003d9c",
        "Pointer_jp": "82345af0",
        "String_en": "Gamer Card display",
        "String_jp": "ゲーマーカード表示"
}
It is presented in the following way: 
data = [elem1, elem2, ..., elemN]
for elem in elems: elem['Location'] = original position, elem['Pointer_jp'] = pointer that tracks said position, elem['String_jp'], elem['String_en']

We want to replace the string_jp in the executable by its corresponding string_en. There are subtleties:
    - Some of our strings are bigger than the original ones. When such a thing happens, we need to offset the position of the next string.
        Example: If we stand at position 0x1000 and initially have a string_jp of length 0x8, and that our string_en is of length 0xc, we are 0x4 too far.
            We then need to keep the offset of 0x4 in memory, add a 0 at position 0x1008 + offset + 0x1, and make the next string start at position 0x1008 + offset + 0x1 + 0x1
    - Some of our strings are smaller than the original ones. When such a thing happens, we don't have anything to do.
    - Special case: some japanese strings take more space than their encoding. 
        Explanation: some strings take up only two SJIS characters, so 4 bytes, yet take up 8.
            We could enforce , and assume, that a japanese string doesn't have a length smaller than 8. Would it be useful though ?
    - If two strings are more than 0x10 apart, there's probably some  code in-between, better not touch that -> reset offset to 0
    - Special case 2: sometimes we'll write strings that are smaller than their original data, what to do in that case ?
            

"""

import pandas as pd
import json
import hexdump

#150 ok
max = 700

with open('sorted.json', "r", encoding="utf-8") as file:
    #load JSON file and sort rows by the location of the string in memory
    string = file.read()
    data = json.loads(string)
    #prepare variables that we'll use in the loop, temporary stuff and the constant to offset from file to .xex
    offset = 0
    prev = "0"
    in_file = 0x81ffe000 #this is the offset for a string's location
    in_file_pointer = 0x82006000 #this is the offset for a string pointer's location
    location_updated = 0
    len_prev = 0
    loc_initial_prev = ""
    with open('japanese.xex', 'r+b') as xex:
        i = 1
        for obj in data:
            if i > max:
                break
            print(obj)
            location_cur = obj['Location']
            print(f"previous location {hex(int(prev, 16) - len_prev)}-{prev} ; current location {location_cur}") 
            if (loc_initial_prev != location_cur) and (prev == '0' or (prev != '0' and(int(location_cur, 16) != int(prev, 16) - len_prev))):
                location_updated = int(location_cur, 16)
                #if we are stepping over the previous data (so let's say 0x80-0x90 and we're on 0x88) we skip bytes until we're good
                if prev != '0':
                    if(int(prev, 16) >= int(location_cur, 16)):
                        print(f"{location_cur} in conflict with {hex(int(prev, 16) - len_prev)[2:]}-{prev}")
                        offset = (int(prev, 16)) - int(location_cur, 16)
                        xex.seek(int(location_cur, 16) - in_file + offset)
                        print(f"byte written at position {hex(int(location_cur, 16) - in_file + offset)}")
                        offset += 1
                        location_updated += offset
                
                        xex.write('\0'.encode('shift-jis'))
                #if we skipped a little amount of data and haven't zeroed out the original japanese text, we'll do it now
                    elif (abs(int(prev, 16) - int(location_cur, 16)) < 3):
                        print(f"There are some bytes between {prev} and {location_cur}, let's zero them out")
                        for j in range (1, int(location_cur, 16) - int(prev, 16)):
                            
                            xex.seek(int(prev, 16) + j - in_file)
                            print(f"writing null byte at position {hex(xex.tell())} (to fill previous space)")
                            xex.write('\0'.encode('shift-jis'))
                
                
                
                xex.seek(location_updated - in_file)
                en_sjis = obj['String_en'].encode('shift-jis')
                print(f"writing {en_sjis} into file:")
                print(hexdump.dump(en_sjis, sep=" "))
                xex.write(en_sjis)
                
                
                
                encoded_jp = len(obj['String_jp'].encode('shift-jis'))
                """
                if encoded_jp < 8:
                    encoded_jp = 8
                """
                encoded_en = len(en_sjis)
                print(f"{hex(location_updated - in_file)[2:]}; {encoded_en} - {encoded_jp}")
                offset += (encoded_en - encoded_jp)
                
                len_prev = encoded_en

                    
                if (encoded_en < encoded_jp):
                    for j in range(encoded_jp - encoded_en):
                        print(f"writing null byte at position {hex(xex.tell())} (to fill)")
                        xex.write('\0'.encode('shift-jis'))
                        #len_prev += 1
                
                else:
                    print(f"writing null byte at position {hex(xex.tell())} (to delimit)")
                    xex.write('\0'.encode('shift-jis'))
                    len_prev += 1

                prev = str(hex(location_updated + encoded_en))
                loc_initial_prev = obj['Location']
            else:
                print(f"pointer {obj['Pointer_jp']} is for the same data as before ({loc_initial_prev})")
            try:
                xex.seek(int(obj['Pointer_jp'], 16) - in_file_pointer)
            except Exception as e:
                print("error " + str(e)  + ": " + hex(location_updated))
            
            try:
                print(f"Modified pointer at coordinate 0x{obj['Pointer_jp']} (in-file {hex(int(obj['Pointer_jp'], 16) - in_file_pointer)}) to {hex(location_updated)}\n")
                xex.write(location_updated.to_bytes(4, byteorder='big', signed=False))
            except Exception as e:
                print("error " + str(e)  + ": " + hex(location_updated))
            i += 1
            
           
        
