# Veteriner Uygulaması

Uygulama veterinerlerin kayıt tutması için python django kullanılarak geliştrilimiştir.

- Python 3.9
- Django 4.0



## Uygulama Kurulumu

Bilgisayarınızda python3.9 sürümü yüklü değilse ilk olarak python3.9 versiyonunu yükeleyiniz
aksi takdirde  versiyon hatası alacaksınız.

Ardından bilgisayarınıza  pipenv kurunuz.
### Linux
```sh
sudo apt install pipenv
```
### MacOS
```sh
brew install pipenv
```

### Windows
```sh
pip3 install pipenv
```
### İndirme
```sh
git clone https://github.com/bekiryildirimcode/django-veterinary.git
```

### Çalıştırma
```sh
cd django-veterinary            //dizine giriş yapıyoruz
pipenv install                 //bağımlıkları kurun
pipenv shell                  //pipenv ile sanal ortamı etkinleştirin
python manage.py migrate     // Veritabanı tabloları oluştur
python manage.py runserver  // Suncuyu ayağa kaldırın
```

Super Kullancı oluşturmak

```sh
python manage.py createsuperuser
//Kodu çalıştırdıktan sonra çıkan alanları doldurnuz

Username: Superusername
Email address: example@mail.com
Password: ******  
Password(again): ******
```

## Önemli
Kullanıcı kayıt olduğunda default olarak veri silemez.
Kullancıya silme izni vermek için url/admin  yolundan oluşturduğunuz super user ile giriş yapıp
kullanıcını role parametresini akif etmeniz gerekmektedir.


