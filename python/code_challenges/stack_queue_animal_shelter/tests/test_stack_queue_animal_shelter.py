from ..stack_queue_animal_shelter import AnimalShelter
import pytest

def test_create_empty_shelter():
    animal_shelter = AnimalShelter()
    actual = animal_shelter.storage_stack.top
    expected = None
    assert actual == expected

def test_enqueue_one():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('Fluffy', 'Cat')
    actual = animal_shelter.storage_stack.top.value.name
    expected = 'Fluffy'
    assert actual == expected

def test_enqueue_multiple():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('Fluffy', 'Cat')
    animal_shelter.enqueue('Rex', 'Dog')
    animal_shelter.enqueue('Mr. Kayden', 'Cat')
    actual = animal_shelter.storage_stack.top.value.name
    expected = 'Mr. Kayden'
    assert actual == expected

def test_dequeue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('Fluffy', 'Cat')
    animal_shelter.enqueue('Rex', 'Dog')
    animal_shelter.enqueue('Mr. Kayden', 'Cat')
    actual = animal_shelter.dequeue().name
    expected = 'Fluffy'
    assert actual == expected

def test_dequeue_with_dog_preference():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('Fluffy', 'Cat')
    animal_shelter.enqueue('Rex', 'Dog')
    animal_shelter.enqueue('Mr. Kayden', 'Cat')
    actual = animal_shelter.dequeue('dog').name
    expected = 'Rex'
    assert actual == expected

def test_dequeue_with_cat_preference():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('Fluffy', 'Cat')
    animal_shelter.enqueue('Rex', 'Dog')
    animal_shelter.enqueue('Mr. Kayden', 'Cat')
    actual = animal_shelter.dequeue('cat').name
    expected = 'Fluffy'
    assert actual == expected

def test_dequeue_with_no_preference():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('Mr. Kayden', 'Cat')
    animal_shelter.enqueue('Fluffy', 'Cat')
    animal_shelter.enqueue('Rex', 'Dog')
    actual = animal_shelter.dequeue().name
    expected = 'Mr. Kayden'
    assert actual == expected

def test_dequeue_until_empty():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('Mr. Kayden', 'Cat')
    animal_shelter.enqueue('Fluffy', 'Cat')
    animal_shelter.enqueue('Rex', 'Dog')
    actual = animal_shelter.dequeue()
    actual = animal_shelter.dequeue()
    actual = animal_shelter.dequeue()
    with pytest.raises(Exception):
        actual = animal_shelter.dequeue()
