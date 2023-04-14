print("HOŞGELDİNİZ...Yaşanan afetin yaralarını hep birlikte saracağız.")
kullaniciadi='eminergcms'
parola='23py23'

giris=""""
(sisteme üye olmadan bu sistemi kullanamazsınız!!)
1-sisteme üye ol
2-sisteme giriş yap
3-şifremi unuttum
4-sisteme geçiş
q-çıkış yap
"""

print(giris)

while True:
    ss= input("Yapmak istediğiniz işlemin numarasını veya harfini girin:")
    if(ss=='q'):
        print('çıkılıyor...')
        break
    elif(ss=='1'):
        print("sisteme üye ol seçeneğini seçtiniz")
        tc=int(input('TC kimlik numaranızı giriniz:'))
        adsd=input('adınızı ve soyadınızı girin:')
        kaolustur=input('kullanıcı adı oluşturun:')
        dy=int(input('doğum yılınızı giriniz:')) 
        yas=(2023-dy)   
        c=input('cinsiyetinizi giriniz:')
        telno=int(input('Telefon numaranızı başında 0 olmadan giriniz:'))
        print('üyeliğiniz oluşturulmuştur, kişisel bilgileriniz;')
        print(f'Merhaba {adsd} tekrardan hoşgeldiniz teyit amaçlı kişisel bilgilerinizin kontrolü sağlanacaktır.kullanıcı adınız {kaolustur}, TC:{tc}, yas:{yas}, cinsiyet:{c}, telefon numarası:{telno}')




    elif(ss=='2'):
        print("sisteme giriş yapseçeneğini seçtiniz kullanıcı adınızı ve parolanızı girin")
        ka=input('kullanıcı adınızı giriniz:')
        if(ka==kullaniciadi):
          print('kullanıcı adınız doğrudur')
        else:
          print('böyle bir kullanıcı bulunmamaktadır lütfen tekrar deneyiniz.')
    
    # result=(ka==kullaniciadi)
    # print(result)
        prl=input('parolanızı giriniz:')
        if(prl==parola):
          print('sisteme hoşgeldiniz')
        else:
          print('girdiğiniz parola yanlıştır')


    elif(ss=='3'):
         while True:
             print('şifremi unuttum seçeneğini seçtiniz.')
             ys=input('oluşturmak istediğiniz yeni şifrenizi giriniz:')
             ts=input('Lütfen oluşturduğunuz yeni şifrenizi tekrar giriniz:')
             if not ys:
                   print("parola oluşturmadan işleme devam edemezsiniz!")
             elif len(ys)>12 or len(ys)<5:
                   print("parola 12 karakterden uzun 5 karakterden kısa olmamalı") #döngüye sok tekrar şifre girsin
             elif(ys==ts):
                   print('yeni şifreniz oluşturuldu.')                    
             else:
                 print('şifreler birbiriyle uyuşmamaktadır')
             break

    # elif(ss=='3'):
    #     print('şifremi unuttum seçeneğini seçtiniz.')
    #     ys=input('oluşturmak istediğiniz yeni şifrenizi giriniz:')
    #     ts=input('Lütfen oluşturduğunuz yeni şifrenizi tekrar giriniz:')
    #     if(ys==ts):
    #       print('yeni şifreniz oluşturuldu.')
    #     else:
    #       print('girdiğiniz şifre birbiriyle uyuşmamaktadır') #döngüye sok tekrar şifre girsin
    else:
        print('....YANLIŞ GİRİŞ....')
        print("Aşağıdaki seçeneklerden birini giriniz:", giris)







    
