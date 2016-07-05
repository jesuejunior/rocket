# # encoding: utf-8
# from django.db import models
#
# from engine.models.container import Container
# from engine.models.spacebus import Spacebus
#
#
# class SpacebusHasContainer(models.Model):
#
#     """
#     """
#     spacebus = models.ForeignKey(Spacebus)
#     container = models.ForeignKey(Container)
#
#     class Meta:
#         db_table = u'spacebus_has_container'