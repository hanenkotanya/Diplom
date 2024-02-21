from django.db import models
from PIL import Image


class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    image1 = models.ImageField(blank=True, null=True,
                              upload_to='media/', verbose_name="Первая страница меню")
    image2 = models.ImageField(blank=True, null=True,
                              upload_to='media/', verbose_name="Вторая страница меню")
    image3 = models.ImageField(blank=True, null=True,
                              upload_to='media/', verbose_name="Третяя страница меню")
    mini_image = models.ImageField(blank=True, null=True,
                              default='media_mini/default.jpg',
                              upload_to='media_mini/', verbose_name="Фото для миниатюры для общей страницы с ресторанами")
    

    def __str__(self):
        return 'Меню ресторана {}'.format(self.name)
    
    
    def save(self):
        super().save()
        img_mini = Image.open(self.mini_image.path)
        path=self.mini_image.path
        print(self.mini_image.path)
        self.mini_image=img_mini
        if img_mini.height > 300 or img_mini.width > 300:
            output_size = (300, 300)
            img_mini.thumbnail(output_size)
            img_mini.save(path)



    

