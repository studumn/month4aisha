
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
       
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('card_number', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Выполнено', 'Выполнено'), ('Не выполнено', 'Не выполнено')], default='Не выполнено', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.book')),
            ],
        ),
    ]
