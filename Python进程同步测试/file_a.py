import data

# def change_a(a):
#     a =  'a changed'
#     b = input('plz input:')
#     return a, b 

if __name__ == '__main__':
    # ca, cb = change_a(data.a)
    print(f'before file_b.py run, data.a is {data.a}')
    b = input('waiting for file_b.py......')
    print(f'after file_b.py run, data.a is {data.a}')
    # print(data.b)