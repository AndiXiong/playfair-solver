import math
import random

import ngram_score as ns
from modify_key import modify_key


ciphertext = "SPPDNQSPELYSGDOCCYOFRWARZIIWLQPCNOARQUHCURWQGECOECZTARURQHRUDZNDMTBTWYZIIWOYLCLIENCIOMTBYSKOSPEGRWARZEYOLPOCQXELPGRKWEDNZPFEQWELUGLIENBXNCZIIPKROFELPSQODNXUILONLUCNQXELKDNPQOONZQNDQWEHBEFGHOZIYWBUURGZSRZIWPLQVYHPKPNMKMZIYWASFGWQZIWESPXIWERWARZEYOIWELEMYOHPXBLUCLOZTBLDEVWERWARFEYPDUMQPMURQSLENEGZYOWPSPZIHPKPOYKOCPECZTARSPCDNOSPICYOECZTARZIURVYDFZIYWQCYOURONCIKRKSLQCNDABKLQHZYTONXQCPZIBMZILHPWOYOYNFTBHOECZTARONDNZIMRQOELNKQYLOGDPULOMBCLZESUAERSHABMZILHLIENPESPXIWERWARZEYOIWELLKNPQOICYOIMEYDFZILHOLHOHOWQARCYZIYWECXKNDMBUIHOQWABWQOLRSIMELVHNYZINPHZWQKUNFWIWKRWARURGDBYOGRWARPWXABZCDASFGWQDWECZTARUROGYUYTEYPUDNTYPHONMIHPECZTARPSHQZIWPNWNOAROFRWARBMYUBZHBYSXUHFIWAMELRKZQQWURQHDZUYHFIWAMAQBYDUECZTARSROHQZELPGRKWEDNTERELNXUIHONMBQOHBYSXUHFIWAMECANSKWERWARPSHQZILIEQQXEDSFIZLNXUIHONMBQOHBYSXUHFIWASFGWQYRDUSPECZTARKOYLNZONDNZIEKRWARFESUBEDFELDYURGDONWQEGRWARILXBUZBZRKXVNDZILWYWYOUYOGTBIMRWNDDNXMEYBZELHRWEHQHOWQONONMTZILOLWZQRMZILHKPXUILQZELTERFYLBZDCIWELKRQOASOHZIYWCDNOAIHOQWZIWPLQVYHPPWOYPDNMKMWQYSCIZIYWCDECZTARURQZELHESRKDCPDUNCNQONVXELBTOXNWNOARQXYSMTZILHPIFZCHGZYTWQBZRMURODNXWCCIQMELARQOZILHLIENXEURONVXELPWBZONXVLQQHDFZILHPWOYOHWIKALQHOWQCDECZTARZIWPLQVYHPKSCIWQWQURQZELIYNQYPGESKNEOHOFNEYUKRQOWQONDNZIIMELEAOYPHQXHOSAYPBXLVNXAQPKLIIWBZSNOHOZTBZGYBWRQOPSQOWQZIHPKPOYKOCPZILHKSCISKNEGZYPOHOZUYVYDFBZEVGFRWARWQCYWOEYXKDNZAXBTAIYDFURQZQWELBTOXNWNOARQXELERLUCLOYRSBHIFYOQEEFURECZTARLQYUHQTEZICDHNURGDIWTEZIAOWEEQBPYLPWHUONWICIKMNQWCVXELMQBKLIYOAZSRIWELTERFYLPSAOIWMIPULWWEEYQDIWANOFRWARURRSXUHUEDRCYSQOPZTBIZELXAQXYIZILYKRKAPSGEHOONZQNDQWEHPWQXWQZIWPTBGEPGBUPQRKQZNCYIIEYOASAGIWTEZICNNOCNQMELEQANOLEKRWARURQZELOYDZHPPMZIHCNEOHOFSUONZBELMQYLQHWQDLYOCPDLYPRSQOCNNFQZYSBTXVTBWIGZYOLWPKXIHRQWDZHOHQQNMVQNMPRLZILQKSPQBXZIWEYSKANCZIHCNEOHOFSUECZTARABZBELPSXMYSBTMXSPAOIWMIECZTARPDDZYWSRLPSEYOTYQOWQPWRKTBUROGRKKMELDANFPQFUOLBTQXELASAGIWONMTZILOECZTARPILQCSOYUSOYNGNDZILYNPDQLHECZTARZILHUYHUMBQMHOCNQMELYWYOUYOGTBMRQOZIWPLQVYHPKSCIZIYWZIOYWEELYOPSQOARRLCDNOTEDZHPWQKPNMKMTEZIZIYWONMINPTEXUYNYWYWPIQMELOYMPUDNDRPOQQWICLOSUBMEZRMPIMXLWLOZIWESPXIWCVXELTEFGHOTEWVYSQOZILWYWYOUYOGTBHRQWZELOZILCNPQMKRCIILDAPWQXLQPHRKGENCZIWPTBGEDZLESRPHLOZIYWECTYDFECZTARURGDDPLOMTZIWPLQCHRZNQCYHAWQAQLQVZELZMDEYOONBTMXSPXAGEYSDOYOWQVLQOZILYOMRMASFGZIDNSFIZELQTCVYLHNPDVUBXWIOKBUPSQOHLXUENZOBYBHHPZIURTBMPPALYDFKPNMQYHOONMTZILHFRWPECZTARNCECANPHECZTARZILHXABZCDBZKRHVIZYPBZECZTARWQMPDOZIYOHBLQHDNFURQZELHAMBQMHONCVLQXELQYHZMXRMONBQBXBMQNNQECZTARZELOZIHPNFMPPDCIQMELYQELSRPGRWARZILHQHOQQWFRCPZEEVEZSPYPBZUROZEYGEMPPZHPWVRWARURQZYSMXSPZIYOYPPDQXELEMYOLIDPBTQXELKDYPXVYLHNDGQWZILHCYBWNQMPYFLQCFRWAREDPWCIOKRWARURRSXQHVIZZIYWNWNQKPWYNPMBQODZNQIPQYHZXILM"
ALPHABETS = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

# TABLE = [
#     ['A', 'B', 'C', 'D', 'E'],
#     ['F', 'G', 'H', 'I', 'K'],
#     ['L', 'M', 'N', 'O', 'P'],
#     ['Q', 'R', 'S', 'T', 'U'],
#     ['V', 'W', 'X', 'Y', 'Z']
# ]

def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char = char))


def decrypt_playfair(table):
    assert(len(ciphertext) % 2 == 0)
    res = ''
    for index in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[index], ciphertext[index+1]
        letter1_x, letter1_y = find_in_list_of_list(table, letter1)
        letter2_x, letter2_y = find_in_list_of_list(table, letter2)
        # print(letter1_x, letter1_y, letter2_x, letter2_y)
        if letter1_x != letter2_x and letter1_y != letter2_y:
            d_letter1 = table[letter1_x][letter2_y]
            d_letter2 = table[letter2_x][letter1_y]
        elif letter1_x == letter2_x:
            d_letter1 = table[letter1_x][(letter1_y-1) % 5]
            d_letter2 = table[letter2_x][(letter2_y-1) % 5]
        elif letter1_y == letter2_y:
            d_letter1 = table[(letter1_x-1) % 5][letter1_y]
            d_letter2 = table[(letter2_x-1) % 5][letter2_y]
        res += d_letter1 + d_letter2
    return res


def matrix_to_string(table):
    string = ""
    for i in range(len(table)):
        for j in range(len(table[i])):
            string += table[i][j]
    return string

def string_to_matrix(string):
    table = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(string[i*5+j])
        table.append(row)
    return table


def random_key():
    l = list(ALPHABETS)
    random.shuffle(l)
    return string_to_matrix(''.join(l))


if __name__ == "__main__":
    max_score = -math.inf
    bigram = ns.ngram_score('english_bigrams.txt')
    trigram = ns.ngram_score('english_trigrams.txt')
    quadgram = ns.ngram_score('english_quadgrams.txt')
    i, last_i = 0, 0
    while True:
        key = random_key()
        print("Iteration: {}".format(i))
        last_i = i
        while i - last_i < 2000:
            new_key = [row[:] for row in key]
            new_key = modify_key(new_key)
            deciphered_text = decrypt_playfair(new_key)
            score = bigram.score(deciphered_text) + trigram.score(deciphered_text) + quadgram.score(deciphered_text)
            # print("Iteration: {}; Score: {}; Key: {}; Text: {}".format(i, score, matrix_to_string(key), deciphered_text))
            i += 1
            if score > max_score:
                max_score, key, last_i = score, new_key, i
                print("Iteration: {}; Score: {}; Key: {}; Text: {}".format(i, score, matrix_to_string(key), deciphered_text))
