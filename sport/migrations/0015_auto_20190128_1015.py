# Generated by Django 2.1.5 on 2019-01-28 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0014_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketballImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(default='', max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='general_images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BasketballPlayerInBasketballGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_player', models.BooleanField(blank=True, null=True)),
                ('time_of_change', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BasketballTeamInBasketballGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_score', models.IntegerField(blank=True, null=True)),
                ('property_percent', models.IntegerField(blank=True, null=True)),
                ('situation', models.CharField(blank=True, choices=[('AW', 'برد'), ('BE', 'مساوی'), ('CL', 'باخت')], max_length=3, null=True)),
                ('best_player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballPlayer')),
            ],
        ),
        migrations.CreateModel(
            name='BasketballVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(default='', max_length=250)),
                ('video', models.FileField(blank=True, null=True, upload_to='general_videos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='footballimage',
            old_name='football_game',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='footballvideo',
            old_name='football_game',
            new_name='game',
        ),
        migrations.RemoveField(
            model_name='basketballgame',
            name='teams',
        ),
        migrations.AddField(
            model_name='basketballgame',
            name='league',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballLeague'),
        ),
        migrations.AddField(
            model_name='basketballvideo',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballGame'),
        ),
        migrations.AddField(
            model_name='basketballteaminbasketballgame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballGame'),
        ),
        migrations.AddField(
            model_name='basketballteaminbasketballgame',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballTeam'),
        ),
        migrations.AddField(
            model_name='basketballplayerinbasketballgame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballGame'),
        ),
        migrations.AddField(
            model_name='basketballplayerinbasketballgame',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballPlayer'),
        ),
        migrations.AddField(
            model_name='basketballimage',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport.BasketballGame'),
        ),
        migrations.AddField(
            model_name='basketballimage',
            name='news',
            field=models.ManyToManyField(blank=True, null=True, to='sport.News'),
        ),
    ]
