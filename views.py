from Finance.models import User,Transaction
from Finance.forms import TransactionForm, UserForm
from django.shortcuts import render,redirect
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect

# Create your views here.
def add_transaction(request):
    if(request.method == 'POST'):
        user_form = UserForm(request.POST)
        transaction_form = TransactionForm(request.POST)
        if (user_form.is_valid() and transaction_formset.is_valid()):
            user = user_form.save()
            transaction_form.cleaned_data['user_id'] = user
            transaction = transaction_form.save()
            return HttpResponseRedirect(request,'Finance/index.html', {})
        else:
            print('Failed')
      else:
        user_form = UserForm()
        transaction_formset = TransactionForm()
    return render(request,'Finance/add_transaction.html', {
            'user_form':user_form,
            'transaction_form': transaction_form,
        })

def add_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = UserForm()
        return render(request, 'Finance/index.html', {
            'form': form
        })




def show_users(request):
    users = User.objects.all()
    return render(request, 'Finance/show.html', {
        'user' : users
    })

def show_transaction(request):
    transaction = Transaction.objects.all()
    return render(request, 'Finance/show.html', {
        'transaction' : transaction
    })

def edit_transaction(request):
    edit_trans = Transaction.objects.get(id=id)
    return render(request,'Finance/edit.html',{
        'edit_transaction':edit_trans
    })


def edit_users(request):
    edit_user = User.objects.get(id=id)
    return render(request,'Finance/edit.html',{
        'edit_users':edit_user
    })

def delete_transaction(request):
    del_trans = Transaction.objects.get(id = id)
    del_trans.delete()
    return redirect('Finance/show')


def delete_users(request):
    del_user = User.objects.get(id = id)
    del_user.delete()
    return redirect('Finance/show')

