import unittest
import RunnerTest
import TournamentTest

RtTs = unittest.TestSuite()
RtTs.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
RtTs.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(RtTs)