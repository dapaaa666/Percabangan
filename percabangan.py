#!/usr/bin/env python
# coding: utf-8

# In[11]:


#menentukan ganjil geanap
nilai = int(input('Isikan Nilai'))
sisa_bagi = nilai % 2

if sisa_bagi==0:
    print(f'{nilai} adalah bilangan genap')
else:
    print(f'{nilai} adalah bilangan ganjil')
    
print('Program Selesai')


# In[22]:


#0-49= e
#50-59= d
#60-69= c
#70-84= b
#85-100= a

nilai_program = int(input('Isikan Nilai Pemrograman:'))
if nilai_program < 0 or nilai_program > 100:
    print("Nilai anda salah")
else:
    if nilai_program <50:
        print ("e")
    elif nilai_program <60:
        print ("D")
    elif nilai_program <70:
        print ("C")
    elif nilai_program <85:
        print ("B")
    elif nilai_program <100:
        print ("A")
    else:
        print("Input anda salah")


# In[28]:


username = input('Isikan Username')
password = input('Isikan Password')

#jika username salah => username anda salah
#jika password salah => password anda salah
#jika keduanya salah => username dan password anda salah
#jika keduanya benar => selamat datang {username}
#username: admin
#password: admin

if username == 'admin':
    if password == 'admin
    
        print(f'Selamat Datang {username}')
else:
    if password == 'admin':
        print("Username anda Salah")
    else:
        print("Username dan Password anda Salah")


# In[46]:


nama = input("Masukan nama:")
umur = int(input("Masukan umur:"))
alamat = input ("Masukan alamat:")
tabungan = int(input("Masukan tabungan:"))

pangkat = ''
if umur > 40:
    if alamat == 'New York' or alamat == 'Nevada' or alamat == 'Havana':
        if tabungan > 10000000:
            pangkat = 'Don'

pangkat = ''
if umur > 25:
    if alamat == 'New Jersey' or alamat == 'Manhattan' or alamat == 'Nevada':
        if tabungan > 1000000:
            pangkat = 'Underboss'
            
pangkat = ''
if umur > 18:
    if alamat == 'California' or alamat == 'Detroit' or alamat == 'Boston':
        if tabungan < 1000000:
           pangkat = 'Capo'
            
if pangkat != '':
    print(f'{nama} kemungkinan seorang anggota mafia dengan pangkat {pangkat}')
else:
    print(f'{nama} tidak mencurigakan')

