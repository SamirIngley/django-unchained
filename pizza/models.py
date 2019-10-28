from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    topping = models.ManytoMany(toppings)

    if __name__ == "__main__":
        return self.name

class Toppings(models.Model):
    question = models.ForeignKey(pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    if __name__ == "__main__":
        return self.name
