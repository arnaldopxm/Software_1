import unittest
from servicios import *

class calcularPrecioTester(unittest.TestCase):
	def testSameDay14min(self):
		i = datetime.datetime(2017,1,23,10,40)
		j = datetime.datetime(2017,1,23,10,44)
		tarifa = Tarifa(10,100)
		self.assertEqual(0,calcularPrecio(tarifa,[i,j]))

	def testDiferentDay14min(self):
		i = datetime.datetime(2017,1,23,23,59)
		j = datetime.datetime(2017,1,24,0,5)
		tarifa = Tarifa(10,100)
		self.assertEqual(0,calcularPrecio(tarifa,[i,j]))	

	def testDiferentMonth14min(self):
		i = datetime.datetime(2017,1,31,23,50)
		j = datetime.datetime(2017,2,1,0,5)
		tarifa = Tarifa(10,100)
		self.assertEqual(0,calcularPrecio(tarifa,[i,j]))

	def testDiferentYear14min(self):
		i = datetime.datetime(2016,12,31,23,50)
		j = datetime.datetime(2017,1,1,0,5)
		tarifa = Tarifa(10,100)
		self.assertEqual(0,calcularPrecio(tarifa,[i,j]))

	def test15min(self):
		i = datetime.datetime(2017,1,23,10,40)
		j = datetime.datetime(2017,1,23,10,55)
		tarifa = Tarifa(10,100)
		self.assertEqual(10,calcularPrecio(tarifa,[i,j]))

	def testSemana_FindeSemana24horas(self):	
		i = datetime.datetime(2017,1,27,15,00)
		j = datetime.datetime(2017,1,28,15,30)
		tarifa = Tarifa(10,100)
		self.assertEqual(1590,calcularPrecio(tarifa,[i,j]))


	def testSemana_Semana24horas(self):	
		i = datetime.datetime(2017,1,24,15,00)
		j = datetime.datetime(2017,1,26,15,30)
		tarifa = Tarifa(10,100)
		self.assertEqual(480,calcularPrecio(tarifa,[i,j]))

	def testFin_Semana_Fin_Semana24horas(self):	
		i = datetime.datetime(2017,1,28,15,00)
		j = datetime.datetime(2017,1,29,15,30)
		tarifa = Tarifa(10,100)
		self.assertEqual(2400,calcularPrecio(tarifa,[i,j]))


if __name__=="__main__":
	unittest.main ()
	