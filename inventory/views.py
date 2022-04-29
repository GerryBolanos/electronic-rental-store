from django.shortcuts import render, redirect
from .models import Customer, Electronics, Phone, Rents
from .forms import AddNewElectronicForm, RentItemForm, RemoveItemForm
from django.db import connection

'''
    NOTE: To make it easier to follow the necessary steps to get credit for this course, we're opting to use RAW queries
        so that we can create parametrized queries that mimic PreparedStatements in Django, while also
        having the option to call stored procedures and functions. 
'''


# Create your views here.
def index(request):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ELECTRONICS")
        inventory = cursor.fetchall()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM TABLET")
        tablets = cursor.fetchall()
        cursor.execute("SELECT ITEMCOUNT('tablet')")
        tabCount = cursor.fetchone()[0]
        cursor.execute("SELECT ITEMCOUNT('mphone')")
        phoneCount = cursor.fetchone()[0]
        cursor.execute("SELECT ITEMCOUNT('laptop')")
        lptCount = cursor.fetchone()[0]

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM MOBILEPHONE")
        mobilephones = cursor.fetchall()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM LAPTOP")
        laptops = cursor.fetchall()

    context = {
        'queryset': inventory,
        'tablets': tablets,
        'tabCount': tabCount,
        'mobilephones': mobilephones,
        'phoneCount': phoneCount,
        'laptops': laptops,
        'lptCount': lptCount
    }
    return render(request, 'index.html', context=context)


def rented(request):
    with connection.cursor() as cursor:
        cursor.execute("select custId, fname, lname, elecid, rental_date, return_date from CUSTOMER NATURAL JOIN RENTS")
        rented_details = cursor.fetchall()

    context = {
        'rented_details': rented_details
    }
    return render(request, 'rented_equipment.html', context=context)


def new_item(request):
    if request.method == "POST":
        form = AddNewElectronicForm(request.POST)
        if form.is_valid():
            # form.save()
            with connection.cursor() as cursor:

                cursor.execute("INSERT INTO ELECTRONICS(elecid, electype, model, stock, os, screen_size, storage, gpu, refresh_rate, carrier) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               [form.cleaned_data.get("elecid"),
                                form.cleaned_data.get("electype"),
                                form.cleaned_data.get("model"),
                                form.cleaned_data.get("stock"),
                                form.cleaned_data.get("os"),
                                form.cleaned_data.get("screen_size"),
                                form.cleaned_data.get("storage"),
                                form.cleaned_data.get("gpu"),
                                form.cleaned_data.get("refresh_rate"),
                                form.cleaned_data.get("carrier")])

        return redirect("/")
    else:
        form = AddNewElectronicForm()
    return render(request, "add_electronic_form.html", {"form": form})


def remove_item(request):
    if request.method == "POST":
        form = RemoveItemForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                print(form.cleaned_data.get("elecid"))
                cursor.execute("DELETE FROM ELECTRONICS WHERE elecid = %s", [form.cleaned_data.get("elecid")])

            return redirect("/")
    else:
        form = RemoveItemForm()

    return render(request, "remove_item_form.html", {"form": form})


def rent_item(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ELECTRONICS")
        inventory = cursor.fetchall()
        cursor.execute("SELECT custId, fname, lname from CUSTOMER")
        customers = cursor.fetchall()

    if request.method == "POST":
        form = RentItemForm(request.POST)

        if form.is_valid():
           with connection.cursor() as cursor:
               elecId = form.cleaned_data.get("elecid")
               cursor.execute("INSERT INTO RENTS(custid, elecid, rental_date, return_date) VALUES(%s, %s, %s, %s)",
                              [
                                  form.cleaned_data.get("custid"),
                                  form.cleaned_data.get("elecid"),
                                  form.cleaned_data.get("rental_date"),
                                  form.cleaned_data.get("return_date")
                              ])
               cursor.execute("SELECT stock from ELECTRONICS WHERE elecId = %s", [elecId])
               item_stock = cursor.fetchone()[0]
               item_stock = item_stock - 1
               cursor.execute("UPDATE ELECTRONICS SET stock = %s WHERE elecId = %s", [item_stock, elecId])
        return redirect("rented")
    else:
        form = RentItemForm()

    return render(request, "rental_form.html", {"form": form, "inventory": inventory, "customers": customers})
