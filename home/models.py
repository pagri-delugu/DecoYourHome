from django.db import models

class Product(models.Model):
    name           = models.CharField(max_length=200, verbose_name="Tên sản phẩm")
    price          = models.IntegerField(verbose_name="Giá bán")
    discount       = models.IntegerField(default=0, verbose_name="Giảm giá (%)")
    image          = models.ImageField(upload_to='products/', verbose_name="Hình ảnh")
    sold_quantity  = models.IntegerField(default=0, verbose_name="Đã bán")
    origin         = models.CharField(max_length=50, default="Việt Nam", verbose_name="Xuất xứ")
    description    = models.TextField(blank=True, null=True, verbose_name="Mô tả chi tiết")
    in_stock       = models.BooleanField(default=True, verbose_name="Còn hàng?")

    def __str__(self):
        return self.name

    def get_percentage(self):
        return self.discount/100

class Banner(models.Model):
    title     = models.CharField(max_length=200, verbose_name="Tiêu đề Banner")
    image     = models.ImageField(upload_to='banners/', verbose_name="Hình ảnh")
    alt_text  = models.CharField(max_length=100, blank=True, null=True, verbose_name="Mô tả ảnh")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị?")

    def __str__(self):
        return self.title

class Post(models.Model):
    title      = models.CharField(max_length=200, verbose_name="Tiêu đề bản tin")
    content    = models.TextField(verbose_name="Nội dung")
    image      = models.ImageField(upload_to='posts/', verbose_name="Ảnh bìa")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đăng")

    def __str__(self):
        return self.title