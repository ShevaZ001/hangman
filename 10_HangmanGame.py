import random as r

def hangman(word):
    wrong = 0
    stages = ['',
            '__________          ',
            '|         |         ',
            '|         ○        ',
            '|       ／|＼       ',
            '|         |         ',
            '|      　/|         ',
            '|       / /         ',
            '|                   '
            ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False

    print('ハングマンへようこそ！！文字数は',len(word),'文字だよ！')
    print('answer:',' '.join(board))
    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字だけ予想してね！'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print('answer:',' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('\n貴方の勝ち！助かったね！')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('\n貴方の負け！　正解は{}。'.format(word))


ls_animal=['cat','dog','dolphine','monkey','human','mouse','rabbit','lion','tiger','dragon','bird']
i_r=r.randint(0,len(ls_animal)-1)
print('\n====================\nanswer is "',ls_animal[i_r],'" !!!!!!\n====================\n')
hangman(ls_animal[i_r])
