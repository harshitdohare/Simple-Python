def word(a):

    if a[0] in 'aeiou':
        a = a + 'way'
    else:
        no_vowel = 1

        for i in a:
            if i in 'aeiou':
                a = a[1:] + a[0] + 'ay'
                break
            else:
                no_vowel = 0

        if no_vowel == 1:
            a = a + 'ay'

    return a


def translate(str1):
    l = list(str1.split(' '))
    # smallest
    ans = []
    for i in l:
        ii = word(i)
        ans.append(ii)

    print(*ans, sep=' ')


str_input = input('Enter string here: ')
translate(str_input)
