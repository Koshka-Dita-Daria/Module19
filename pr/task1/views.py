from django.shortcuts import render
from models import Buyer, Game
from django.db.models import Count
# import random
# Create your views here.
# B_more_18 = Buyer.objects.filter(age__gte=18)
# B_less_18 = Buyer.objects.exclude(age__gte=18)
# G_with_18 = Game.objects.filter(age_limited__exact=True)
# G_kids = Game.objects.filter(age_limited__exact=False)
# stats = Game.objects.aggregate(
#     total_cost=Count('balance')
# )
# print(stats["total_cost"])
# for games in G_kids:
#     Game.objects.get(games.id).buyer.set(B_less_18)
# for games1 in G_with_18:
#     Game.objects.get(games1.id).buyer.set(B_more_18)
# k = 0
# for gamers in B_more_18:
#     for games in G_kids:
#         if gamers.balance >= stats("total_cost") and k == 0:
#             Game.objects.get(games1.id).buyer.get(gamers.id)
#     k=1
#     if k == 1:
#         break




