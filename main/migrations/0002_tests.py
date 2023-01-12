from django.db import migrations

def create_data(apps, schema_editor):
    Test = apps.get_model('main', 'Test')
    Test(name="Test 1").save()
    Test(name="Test 2").save()
    Test(name="Test 3").save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
