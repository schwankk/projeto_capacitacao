import csv
import os

def cria_csv(file_path, pessoa=False):
    if not(pessoa):
        header = ['Nome',
                'Descrição',
                'Preço']
    else:
        header = ['First Name',
                'Last Name',
                'role',
                'company',
                'adress','email','phone']

    if os.path.exists(file_path):
        os.remove(file_path)

    with open((file_path), 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)


def escreve_csv(file_path, row):
    with open((file_path), 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
