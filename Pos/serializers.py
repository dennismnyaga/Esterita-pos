from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class MaterialSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'
    
    
    
class ProductPropSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = ProductSizeSerializer(read_only=True)
    class Meta:
        model = ProductPro
        fields = '__all__'
    
    
class ProductProSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPro
        fields = '__all__'
        
 
class ProductAndDetailsSerializer(serializers.ModelSerializer):
    prod = ProductProSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'
               

class ProductPropUpdateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ProductPro
        fields = '__all__'
        
        
class StockPropUpdateSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    class Meta:
        model = StockProperty
        fields = '__all__'
        
        
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        
        

        
        

class StockPropertySerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    
    class Meta:
        model = StockProperty
        fields = '__all__'
        
        

class ExpensesSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = Expenses
        fields = '__all__'
        
        
class AddExpensesSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer()
    class Meta:
        model = Expenses
        fields = '__all__'
        
        
    def create(self, validated_data):
        expense = Expenses.objects.create(**validated_data)
        return expense
        
        

        
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
        
  
        


class WorkInProgressSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    
    class Meta:
        model = WorkInProgress
        fields = '__all__'
        
        


class CartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductPropSerializer()
    
    class Meta:
        model = Cart
        fields = '__all__'
        
        

class CartCreateSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
   

    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        print("this is the validated data ", validated_data)
        customer, created = Customer.objects.get_or_create(**customer_data)
        cart = Cart.objects.create(customer=customer, **validated_data)
        return cart
    
    
    
class CreateProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    color = ColorSerializer()
    size = ProductSizeSerializer()
    material = MaterialSerializer()

    class Meta:
        model = ProductPro
        fields = '__all__'

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product_color = validated_data.pop('color')
        product_size = validated_data.pop('size')
        product_material = validated_data.pop('material')
        product, created = Product.objects.get_or_create(**product_data)
        color, created = Color.objects.get_or_create(**product_color)
        size, created = ProductSize.objects.get_or_create(**product_size)
        material, created = Material.objects.get_or_create(**product_material)
        productpro = ProductPro.objects.create(product=product, color=color, size=size, material=material, **validated_data)
        return productpro
    
    
    
    
class CreateStockSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    color = ColorSerializer()
    
    class Meta:
        model = StockProperty
        fields = '__all__'
        
        
    
    def create(self, validated_data):
        material_data = validated_data.pop('material')
        material_color = validated_data.pop('color')
        color, created = Color.objects.get_or_create(**material_color)
        material, created = Material.objects.get_or_create(**material_data)
        stockproperty = StockProperty.objects.create(color=color, material=material, **validated_data)
        return stockproperty
    
    
    
class CreateEmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employees
        fields = '__all__'
        
        
    
    def create(self, validated_data):
        employee = Employees.objects.create(**validated_data)
        return employee
    
    
    
    
    
class CreateProgressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkInProgress
        fields = '__all__'
        
    def create(self, validated_data):
        workInprogress = WorkInProgress.objects.create(**validated_data)
        return workInprogress
    
    
    
    
    

class UserRegSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    # email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            # email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
    
    
    
class AddProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    size = ProductSizeSerializer()
    material = MaterialSerializer()
    class Meta:
        model = ProductPro
        fields = '__all__'

    def create(self, validated_data):
        # product_data = validated_data.pop('product')
        product_color = validated_data.pop('color')
        product_size = validated_data.pop('size')
        product_material = validated_data.pop('material')
        # product, created = Product.objects.get_or_create(**product_data)
        color, created = Color.objects.get_or_create(**product_color)
        size, created = ProductSize.objects.get_or_create(**product_size)
        material, created = Material.objects.get_or_create(**product_material)
        productpro = ProductPro.objects.create( color=color, size=size, material=material, **validated_data)
        return productpro