<p align="center">
  <img src="https://rake.itu.edu.tr/img/rake-white-logo.png" width="350" title="İTÜ Robotik Arama Kurtarma Ekibi">
</p>

# İTÜ RAKE - Yazılım Ekibi Araştırma ve Uygulama Görevleri

## Robot Operating System (ROS) Araştırması

- ROS'u Tanıma Araştırması
- ROS Elemanlarını Öğrenme Araştırması

### ROS'u Tanıma Araştırması
- ROS nedir?
- Robotikte hangi amaçla kullanılır?
- Bir robotik projesinde ROS ve açık kaynak ROS paketi kullanımı hangi seviyede olmalıdır?
- ROS kullanımı nasıl azaltılabilir?

Sorularına karşılık, kendi cümlelerinizle hazırladığınız en az 1 sayfalık cevabı olan bir araştırma olmalıdır.

### ROS Elemanlarını Öğrenme Araştırması
- ROS workspace, nodes, topics, services, master-slave structure, parameter server
- ROS .launch files, .yaml files, CMakelist.txt
- ROS MoveIt Packege
- Gazebo, RViz
 
Yukarıda yer alan kavramları, dosyaları, paketleri ve çeşitli araçları maddeler halinde kendi yorumunuzla
açıklamanız gerekmektedir. Kavramların tanımlarını kaynaklardan okuyup kendi cümlelerinizle yazmanız, daha sonra bu kavramın bir robotu çalıştırırken bize nasıl yardımcı olacağını yorumlamanız gerekmektedir. Bu yorumlamayı [Husky İnsansız Kara Aracı](https://clearpathrobotics.com/husky-unmanned-ground-vehicle-robot/)'nın dosyalarına bakarak da yapabilirsiniz.
<br/><br/>
## Git ve Github Araştırması
- Versiyon kontrol sisteminin ne olduğunu ve ne işe yaradığını,
- Git Versiyon Kontrol Sistemi'ni,
- Temel git komutlarını (pull, fetch, push, add, commit, branch vb.),
- GitHub'ın ne olduğunu ve ne işe yaradığını,
- Temel GitHub işlemlerini

Bilmeniz ve uygulayabilmeniz gerekmektedir. Bu görev için rapor yazılmayacaktır ama gerekli hasssasiyetin gösterilmesi gerekmektedir.
<br/><br/>
## Çarpışma Önleyici Algoritmalar Araştırması
Robotikte önemli bir konu olan çarpışma önleme algoritmalarını (collision avoidance algorithms) araştırmanız gerekmetedir. Bu araştırma için en az 1.5 sayfa olacak şekilde rapor hazırlanması gerekmektedir. Değinilmesi gereken konular şunlardır:
- Çarpışma önleme bir robot için neden önemlidir?
- Afet sonrası ortamlarda çarpışma önleme neden önemlidir?
- Çarpışma önleme hangi ortamda daha zordur?
  - Sadece bir robotun ve etrafındaki statik ortam.
  - Hareket eden objelerin ya da başka robotların olduğu bir ortam.
  
<br/><br/>
<ins>Araştırma Görevleri Hakkında Dipnot</ins>: Araştırma görevleri için rapor yazarken repositorydeki [referans klasöründe](referans) yer alan rapor kurallarına dikkat edilmeli ve rapor formatına uygun bir şekilde yazılmalıdır.
<br/><br/>
## Uygulamalı Görevler

### Gerekli Yazılımların Kurulması

- Ubuntu 20.04 kurulumu
- Ubuntu 20.04 İşletim Sistemi' ne ROS Noetic kurulumu

Yukarıdaki yazılımları arama motoru üzerinde aratarak yazılımların resmi sayfasına ulaşıp kurulumları gerçekleştirmeniz gerekmektedir.

### Python Programlama Dilinde Publisher ve Suscriber Yazımı

- Repository içerinde [python-assigment dosyası](https://github.com/iturake/itu-rake-assignment-23/tree/main/python-assignment) içinde size verilen kodlar üzerinde programları yazmanız beklenmektedir.
- Publisher ile pub.py dosyasında yer alan topic'lerden herhangi birine (rastgele topic seçen fonksiyon tanımlanmıştır) veri göndermeniz, subscriber ile aynı topic üzerinden gönderilen veriyi dinlemeniz gerekmektedir.
- Topic'e veri gönderimi, verinin broker'a gönderilmesi ile sağlanacaktır. (publisher'ın görevi)
- Topic'den veri alımı, broker üzerinde topic'de bekleyen verinin dinlenilmesi ile sağlanacaktır. (subscriber'ın görevi)
