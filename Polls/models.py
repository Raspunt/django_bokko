from django.db import models



class Student_cource(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return str(self.name)



class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class Student(models.Model):
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=300)
    student_cource = models.ForeignKey(Student_cource, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.name)




class Books(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField(blank = True,db_index = True)
    slug = models.SlugField(max_length = 150,unique= True)
    tags = models.ManyToManyField(Tag,blank = True)


    def __str__(self):
        return str(self.title)



