# -*- coding : utf-8 -*-

import os , sys
from datetime import date , timedelta

from abc import ABCMeta , abstractmethod


# Adicionando pasta externa para capturar os modelos
diretorio_atual = os.getcwd()
app = os.path.dirname(diretorio_atual)

sys.path.append(app)


class FactoryRecorrencia(object):

	@staticmethod
	def criar(horario,string):
		
		if string.lower() in ["anos","ano"]:
			return SomadorAnos(horario)

		elif string.lower() in ["meses","mes"]:
			return SomadorMes(horario)

		elif string.lower() in ["dias" , "dia"]:
			return SomadorDia(horario)

		elif string.lower() in ["minutos" , "minuto"]:
			return SomadorMinutos(horario)

class SomadorRecorrencia(metaclass=ABCMeta):

	def __init__(self,horario):
		self.horario = horario

	@abstractmethod
	def somar(self,quantidade):
		raise NotImplementedError("Método 'somar' não implementado")

class SomadorAnos(SomadorRecorrencia):

	def somar(self,quantidade):

		anos = quantidade * 365
		self.horario = self.horario.datetime + timedelta(days=anos)

		return self.horario

class SomadorMes(SomadorRecorrencia):

	def somar(self,quantidade):
		meses = quantidade * 30

		self.horario = self.horario.datetime + timedelta(days=meses)

		return self.horario

class SomadorDia(SomadorRecorrencia):

	def somar(self,quantidade):
		self.horario = self.horario.datetime + timedelta(days=quantidade)

		return self.horario

class SomadorMinutos(SomadorRecorrencia):

	def somar(self,quantidade):
		self.horario = self.horario.datetime + timedelta(minutes=quantidade)

		return self.horario