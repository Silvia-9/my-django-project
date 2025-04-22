from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

def home(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Expense saved successfully.")  # Debugging line
                return redirect('home')  
            except Exception as e:
                print(f"Error saving form: {e}")  # Debugging line
        else:
            print(f"Form errors: {form.errors}")  # Debugging line
    else:
        form = ExpenseForm()

    try:
        expenses = Expense.objects.all()  
    except Exception as e:
        print(f"Error fetching expenses: {e}")  # Debugging line
        expenses = []  # Handle error gracefully by using an empty list

    return render(request, 'budget/home.html', {
        'expenses': expenses,  # Ensure this variable matches the template
        'form': form,
        
    })

def clear_expenses(request):
    try:
        Expense.objects.all().delete()
    except Exception as e:
        print(f"Error clearing expenses: {e}")  # Debugging line
    return redirect('budget:home')  # Redirect to the correct URL name

def calculate_total(request):
    try:
        # Aggregate the total amount
        total = Expense.objects.aggregate(total_amount=Sum('amount'))['total_amount'] 
        if total is None:  # If no expenses exist
            total = 0
        
        # Get the currency code from the first expense (or use default 'GBP')
        first_expense = Expense.objects.first()
        currency = first_expense.currency if first_expense else 'GBP'

        # Format the total amount with 2 decimal places
        formatted_total = f"{total:.2f}"

        # Return both the total and currency in the JSON response
        return JsonResponse({'total': formatted_total, 'currency': currency})
    except Exception as e:
        print(f"Error in calculate_total view: {e}")  # Debugging line
        return JsonResponse({'error': 'An error occurred while calculating the total.'}, status=500)