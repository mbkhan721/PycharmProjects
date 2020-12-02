# Muhammad Khan --- 3D
"""
Fix the following code so that it works correctly for any offset between -25 and 25
OFFSET = 3
# abcdefghijklmnopqrstuvwxyz
#     |  |
# defghijklmnopqrstuvwxyzabc
"""
offset = -25
msg = 'abcdefghijklmnopqrstuvwxyz'
outMsg = ''
for c in msg:
    if c in msg:
        outMsg += msg[(msg.index(c)+offset)%(len(msg))]
print(outMsg)

