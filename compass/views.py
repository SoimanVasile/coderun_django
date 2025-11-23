from django.shortcuts import render, redirect, get_object_or_404
from .models import Instruction
from .forms import InstructionForm


def compass_view(request):
    """
    Handles displaying the list of instructions and adding new ones.
    Path: /compass
    """
    if request.method == 'POST':
        form = InstructionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compass')
    else:
        form = InstructionForm()

    # Get all instructions for the list
    instructions = Instruction.objects.all().order_by('-id')

    context = {
        'form': form,
        'instructions': instructions
    }
    return render(request, 'compass.html', context)


def instruction_detail_view(request, instruction_id):
    """
    Displays details for a specific instruction.
    Path: /instructions/<int:instruction_id>
    """
    instruction = get_object_or_404(Instruction, id=instruction_id)

    # Calculate summary immediately, but we can hide/show it with JS
    summary_data = instruction.get_route_summary()

    context = {
        'instruction': instruction,
        'summary': summary_data,
    }
    return render(request, 'instruction_detail.html', context)


def first_page(request):
    return render(request, 'Home.html')
