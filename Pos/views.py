from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.db.models import Sum
from datetime import datetime, timedelta





from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        # token['first_name'] = user.first_name
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    


def get_fast_moving_products():
    # Calculate the date one month ago from today
    one_month_ago = datetime.now() - timedelta(days=30)
    
    # Query fast-moving products based on your criteria
    fast_moving_products = ProductPro.objects.annotate(
        total_quantity_sold=Sum('quantity', filter=models.Q(cart__delivered=True, cart__date__gte=one_month_ago))
    ).order_by('-total_quantity_sold')[:10]  # Get the top 10 fast-moving products

    return fast_moving_products




@api_view(['GET'])
def fast_moving_products_api(request):
    fast_moving_products = get_fast_moving_products()
    serializer = ProductPropSerializer(fast_moving_products, many=True)
    return Response(serializer.data)



@api_view(['POST', 'GET'])
def all_products(request):
    product = ProductPro.objects.order_by('-date_added')
    serialize = ProductPropSerializer(product, many=True)
    return Response(serialize.data)

@api_view(['POST', 'GET'])
def all_prods(request):
    product = Product.objects.order_by('-date_added')
    serialize = ProductAndDetailsSerializer(product, many=True)
    return Response(serialize.data)

@api_view(['POST', 'GET'])
def all_productsNames(request):
    product = Product.objects.all()
    serialize = ProductSerializer(product, many=True)
    return Response(serialize.data)


@api_view(['POST', 'GET'])
def all_colors(request):
    color = Color.objects.all()
    serialize = ColorSerializer(color, many=True)
    return Response(serialize.data)



@api_view(['POST', 'GET'])
def all_material(request):
    material = Material.objects.all()
    serialize = MaterialSerializer(material, many=True)
    return Response(serialize.data)




@api_view(['POST', 'GET'])
def all_productsize(request):
    pro_size = ProductSize.objects.all()
    serialize = MaterialSizeSerializer(pro_size, many=True)
    return Response(serialize.data)



@api_view(['POST', 'GET'])
def all_emplyees(request):
    employee = Employees.objects.all()
    serialize = EmployeeSerializer(employee, many=True)
    return Response(serialize.data)



@api_view(['POST', 'GET'])
def all_cart(request):
    cart = Cart.objects.all()
    serialize = CartSerializer(cart, many=True)
    return Response(serialize.data)



@api_view(['POST', 'GET'])
def all_customers(request):
    customer = Customer.objects.all()
    serialize = CustomerSerializer(customer, many=True)
    return Response(serialize.data)



@api_view(['POST', 'GET'])
def all_stock_prop(request):
    stock = StockProperty.objects.all()
    serialize = StockPropertySerializer(stock, many=True)
    return Response(serialize.data)


@api_view(['POST', 'GET'])
def all_on_work(request):
    works = WorkInProgress.objects.all()
    serialize = WorkInProgressSerializer(works, many=True)
    return Response(serialize.data)



@api_view([ 'GET'])
def all_expenses(request):
    expenses = Expenses.objects.order_by('-date_posted')
    serialize = ExpensesSerializer(expenses, many=True)
    return Response(serialize.data)


@api_view(['POST'])
def create_or_update_expenses(request):
    print('this is the request data ', request.data)
    serializer = AddExpensesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# @api_view(['POST'])
# def create_or_update_cart(request):
#     print('this is the request data ', request.data)
#     cart_data = request.data
#     product_id = cart_data['product']
#     cart_quantity = cart_data['quantity']
    
#     print('Product id is: ', product_id)
    
#     product = ProductPro.objects.get(id=product_id)
#     product_quantity = product.quantity
#     print('This product is ', product.quantity)
    
#     if cart_quantity >= 0:
#         if cart_quantity <= product_quantity:
#             remaining_product_quantity = product_quantity - cart_quantity
#             ProductPro.objects.filter(id=product_id).update(quantity=remaining_product_quantity)
            
#     print('Remaining product quantity ', remaining_product_quantity)
#     serializer = CartCreateSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     print('this is the error ', serializer.errors)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def create_or_update_cart(request):
    print('this is the request data ', request.data)
    cart_data = request.data
    product_id = cart_data['product']
    cart_quantity = cart_data['quantity']
    
    print('Product id is: ', product_id)
    
    product = ProductPro.objects.get(id=product_id)
    product_quantity = product.quantity
    print('This product is ', product.quantity)
    
    if cart_quantity >= 0:
        if cart_quantity <= product_quantity:
            remaining_product_quantity = product_quantity - cart_quantity
            ProductPro.objects.filter(id=product_id).update(quantity=remaining_product_quantity)
            
            print('Remaining product quantity ', remaining_product_quantity)
            
            serializer = CartCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print('this is the error ', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Cart quantity exceeds product quantity.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid cart quantity.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_cart(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart not found'}, status=404)

    serializer = CartSerializer(cart, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    print('This is the error ', serializer.errors)
    return Response(serializer.errors, status=400)
   
   
@api_view(['PUT'])
def update_work(request, pk):
    try:
        work = WorkInProgress.objects.get(pk=pk)
    except WorkInProgress.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = WorkInProgressSerializer(work, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['PUT'])
def reset_expense(request, pk):
    try:
        expense = Expenses.objects.get(pk=pk)
    except Expenses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ExpensesSerializer(expense, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    
@api_view(['POST'])
def create_product(request):
    serializer = CreateProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['PUT'])
def add_product(request):
    serializer = AddProductSerializer(data=request.data)
    data=request.data
    print('This is the data ', data)
    if serializer.is_valid():
        serializer.save()
        print('this is the payload ', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print('this is the error ', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# @api_view(['POST'])
# def create_progress(request):
#     serializer = CreateProgressSerializer(data=request.data)
#     if serializer.is_valid():
#         try:
#             employee = serializer.validated_data['employee']
#             stock = serializer.validated_data['stock']
#             size = serializer.validated_data['size']

#             # Only update StockProperty if the size is provided
#             if size is not None:
#                 remaining_meters = stock.size - size

#                 # Update the StockProperty
#                 stock.num_of_rolls -= 1  # Reduce the number of rolls by 1
#                 stock.total -= size  # Deduct the used size

#                 # Handle remaining meters
#                 if remaining_meters > 0:
#                     # If there are remaining meters, update the StockProperty
#                     stock.total -= remaining_meters
#                     stock.size = stock.total / stock.num_of_rolls
#                 else:
#                     # If the last roll is used up, set size to 0
#                     stock.size = 0

#                 # Save the updated StockProperty
#                 stock.save()

#             # Create the WorkInProgress instance after updating the stock
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             # Handle any exceptions and return an error response
#             error_message = str(e)
#             return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         # Handle serializer validation errors
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def create_progress(request):
#     serializer = CreateProgressSerializer(data=request.data)
#     if serializer.is_valid():
#         try:
#             employee = serializer.validated_data['employee']
#             stock = serializer.validated_data['stock']
#             size = serializer.validated_data['size']

#             # Only update StockProperty if the size is provided
#             if size is not None:
#                 # Update the StockProperty
#                 stock.num_of_rolls -= 1  # Reduce the number of rolls by 1
#                 stock.total -= size  # Deduct the used size

#                 if stock.num_of_rolls > 0:
#                     # Calculate the new size if there are remaining rolls
#                     stock.size = stock.total / stock.num_of_rolls
#                 else:
#                     # If no rolls are left, set size to 0
#                     stock.size = 0

#                 # Save the updated StockProperty
#                 stock.save()

#             # Create the WorkInProgress instance after updating the stock
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             # Handle any exceptions and return an error response
#             error_message = str(e)
#             return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         # Handle serializer validation errors
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def create_progress(request):
#     serializer = CreateProgressSerializer(data=request.data)
#     if serializer.is_valid():
#         try:
#             employee = serializer.validated_data['employee']
#             stock = serializer.validated_data['stock']
#             size = serializer.validated_data['size']

#             # Only update StockProperty if the size is provided
#             if size is not None:
#                 if stock.num_of_rolls > 1:
#                     # Reduce the number of rolls if it's greater than one
#                     stock.num_of_rolls -= 1

#                 stock.total -= size  # Deduct the used size

#                 if stock.num_of_rolls > 0:
#                     # Calculate the new size if there are remaining rolls
#                     stock.size = stock.total / stock.num_of_rolls
#                 else:
#                     # If no rolls are left, set size to 0
#                     stock.size = 0

#                 # Save the updated StockProperty
#                 stock.save()

#             # Create the WorkInProgress instance after updating the stock
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             # Handle any exceptions and return an error response
#             error_message = str(e)
#             return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         # Handle serializer validation errors
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def create_progress(request):
    serializer = CreateProgressSerializer(data=request.data)
    if serializer.is_valid():
        try:
            employee = serializer.validated_data['employee']
            stock = serializer.validated_data['stock']
            size = serializer.validated_data['size']

            # Determine the number of rolls based on the size
            if size > 0:
                num_of_rolls = stock.total / size
                stock.num_of_rolls = int(num_of_rolls)  # Round down to the nearest integer
            else:
                stock.num_of_rolls = 0  # If size is 0, set rolls to 0

            # Deduct the used size
            stock.total -= size

            # Update the size based on the remaining rolls
            if stock.num_of_rolls > 0:
                stock.size = stock.total / stock.num_of_rolls
            else:
                stock.size = 0  # If no rolls are left, set size to 0

            # Save the updated StockProperty
            stock.save()

            # Create the WorkInProgress instance after updating the stock
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Handle any exceptions and return an error response
            error_message = str(e)
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Handle serializer validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def create_progress(request):
#     serializer = CreateProgressSerializer(data=request.data)
#     if serializer.is_valid():
#         try:
#             employee = serializer.validated_data['employee']
#             stock = serializer.validated_data['stock']
#             size = serializer.validated_data['size']

#             # Only update StockProperty if the size is provided
#             if size is not None:
#                 remaining_meters = stock.size - size

#                 # Update the StockProperty
#                 stock.num_of_rolls -= 1  # Reduce the number of rolls by 1
#                 stock.total -= size  # Deduct the used size

#                 # Handle remaining meters
#                 if remaining_meters > 0:
#                     # If there are remaining meters, update the StockProperty
#                     stock.total -= remaining_meters
#                     stock.size = stock.total / stock.num_of_rolls
#                 else:
#                     # If the last roll is used up, set size to 0
#                     stock.size = 0

#                 # Save the updated StockProperty
#                 stock.save()

#             # Create the WorkInProgress instance after updating the stock
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             # Handle any exceptions and return an error response
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # def create_progress(request):
#     # serializer = CreateProgressSerializer(data=request.data)
#     # if serializer.is_valid():
#     #     serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def create_stock(request):
    print('This is the stock ', request.data)
    
    the_data = request.data
    print('the_data ', the_data['num_of_rolls'])
    num_rolls = the_data['num_of_rolls']
    role_size = the_data['size']
    
    print('the_datas ', the_data['size'])
    
    total = int(num_rolls) * int(role_size)
    print('GG ', total)
    request.data['total'] = total
    # sizes = stock.size + size
    # request.data['size'] = sizes
    serializer = CreateStockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('This is data ', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print('This is the error ', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['POST'])
def create_employee(request):
    serializer = CreateEmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print('This is the error ', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def delete_employee(request, pk):
    print('employee ', request.data)
    try:
        employee = Employees.objects.get(pk=pk)
        print('Employee found ', employee)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_employee(request, pk):
    try:
        employee = Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
def update_product(request, pk):
    myDict = request.data
    formdata = {}
    updates = {}
    try:
        product = ProductPro.objects.get(pk=pk)
        print('Product found ', product, request.data)
        
    except ProductPro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    for key, value in myDict.items():
                if value:
                    formdata[key] = value
    
    if 'quantity' in formdata and formdata['quantity'] != '':
        current_quantity = product.quantity
        new_quantity = formdata['quantity']
        updated_quantity = current_quantity + new_quantity
        
        updates['quantity'] = updated_quantity
        
        
    if 'price' in formdata and formdata['price'] != '':
        updates['price'] = formdata['price']
        
    print('The data is ', updates)
        
                    
    serializer = ProductPropUpdateSerializer(product, data=updates, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('This is the response ', serializer.data)
        return Response(serializer.data)
    print('Error is ', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['PUT'])
# def update_stock(request, pk):
#     try:
#         stock = StockProperty.objects.get(pk=pk)
#         print('Stock found ', stock, request.data)
#     except ProductPro.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     serializer = StockPropUpdateSerializer(stock, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     print('Error is ', serializer.errors)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def update_stock(request, pk):
    print('Data Received ', request.data)
    try:
        stock = StockProperty.objects.get(pk=pk)
        print('Stock found ', stock, request.data)
    except StockProperty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Perform the arithmetic operation
    num_of_rolls = float(request.data.get('num_of_rolls'))
    size = float(request.data.get('size'))
    extrasize = request.data.get('extrasize')
    
    
    if num_of_rolls is not None and size is not None:
        new_total = num_of_rolls * size
        total = float(new_total) + float(stock.total)  # Add the new total to the current total
        request.data['total'] = total
       
        
        
        new_roll = num_of_rolls + stock.num_of_rolls
        print('New rolls ', new_roll)
        new_size = float(size) + float(stock.size)  # Add the new size to the current size
        print('new size ', new_size)
        request.data['size'] = new_size
        request.data['num_of_rolls'] = new_roll
        # bp = request.data['buying_price']
        # nr = request.data['num_of_rolls']
        # request.data['num_of_rolls'] * request.data['buying_price']
        
        
    # if num_of_rolls is not None and size is not None:
        # total = num_of_rolls * size
        # request.data['total'] = total
        # sizes = stock.size + size
        # request.data['size'] = sizes

    serializer = StockPropUpdateSerializer(stock, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        print('Returned data ', serializer.data)
        return Response(serializer.data)
    print('Error is ', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def user_registration(request):
    serializer = UserRegSerializer(data=request.data)
    print('The register data is ', request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print('there is an error ', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)