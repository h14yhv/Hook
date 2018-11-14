import sys, getopt, re

def VnToEng():
    FileCore = open(sys.argv[1], 'a+')
    FileTranslate = open(sys.argv[2], 'r+')

    # open file destination
    if FileTranslate.mode == 'r+':
        content = FileTranslate.read()
        # print 'Content:' , content
        FileTranslate.close()

    # open file source
    if FileCore.mode == 'a+':
        Core = FileCore.read()
        #        print(Core)
        contentCore = Core.splitlines()
        #        print(contentCore)
        i = 0
        while len(contentCore) != i:
            find_item = contentCore[i].split(':')
            #            print(find_item)
            # generate regular expression ignore case sentitive to search
            try:
                re_item_find = re.compile(find_item[0], re.IGNORECASE)
                content, number = re_item_find.subn(find_item[1], content)
            except:
                print 'compile error'
                content.replace(find_item[0], find_item[1])
            if number > 0:
                print 'Success replace ', number, find_item[0], 'to', find_item[1]
            i = i + 1

    # print(content)
    FileTranslate = open(sys.argv[2], 'r+')
    try:
        print 'write file'
        FileTranslate.write(content)
    except:
        print "Error", sys.exc_info()[0]
    FileTranslate.flush()
    FileTranslate.close()
    FileCore.close()

def ReplaceAlgo(content,Old,New):
    # generate regular expression ignore case sentitive to search
    try:
        re_item_find = re.compile(Old, re.IGNORECASE)
        content, number = re_item_find.subn(New, content)
    except:
        print 'compile error'
        content.replace(Old, New)
    if number > 0:
        print 'Success replace ', number, Old, 'to', New

def ReplaceStr(content,Old,New):
    StrOld = Old.split(' ')
    if len(StrOld) > 1:
        ReplaceAlgo(content, Old + ' ', StrOld[0] + '123 ' + StrOld[1] + '123 ')
        return
    ReplaceAlgo(content, Old + ' ', New + '123 ')
    ReplaceAlgo(content, Old + 's ', New + 's123 ')
    ReplaceAlgo(content, Old + 'es ', New + 'es123 ')
    ReplaceAlgo(content, Old + 'ed ', New + 'ed123 ')


def Eng1ToEng():
    FileTranslate.close()
    FileCore.close()


def EngToEng1():
#    FileCore = open(sys.argv[1], 'a+')
#    FileTranslate = open(sys.argv[2], 'r+')

    FileCore = open(Core_path, 'a+')
    FileTranslate = open(Dest_path, 'r+')

    # open file destination
    if FileTranslate.mode == 'r+':
        content = FileTranslate.read()
        # print 'Content:' , content
        FileTranslate.close()

    # open file source
    if FileCore.mode == 'a+':
        Core = FileCore.read()
        #        print(Core)
        CoreOriginal = Core.splitlines()
        #        print(contentCore)

        i = 0
        while len(CoreOriginal) != i:
            #print CoreOriginal
            ReplaceStr(content, CoreOriginal[i], CoreOriginal[i])   #Replace word
            i = i + 1

    # print(content)
    FileTranslate = open(Dest_path, 'r+')
    try:
        print 'write content to file'
        FileTranslate.write(content)
    except:
        print "Error", sys.exc_info()[0]
    FileTranslate.flush()
    FileTranslate.close()
    FileCore.close()



def main():
    print 'So tham so:', len(sys.argv), 'tham so.'
    print 'Danh sach tham so:', str(sys.argv)

    print 'Usage: File_Core File_Translate Type'
    print "Type: 1: VnToEng, 2:EngToEng1, 3:EngToEng"

#    Type = sys.argv[3]
    Type = 2
    if Type == 1:
        print 'Vn To Eng'
        VnToEng()
    elif Type == 2:
        print 'Eng To Eng1'
        EngToEng1()
    elif Type == 3:
        print 'Eng1 To Eng'
        Eng1ToEng()
    else:
        print 'Error'


Core_path = "E:\\Auto\\TranslateTool\\Translate\\Translate\\test\\Core_eng.txt"
Dest_path = "E:\\Auto\\TranslateTool\\Translate\\Translate\\test\\Dest_eng.txt"
main()
