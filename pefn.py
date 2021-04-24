import pickle
import time


class math:
    def __init__(self, ignore_primes_file=False):
        self.u = utility()
        if not ignore_primes_file:
            self.known_primes = self.u.lod("assets/bigprime.pickle")
        else:
            self.known_primes = [2, 3]

    def flush_known_primes(self):
        self.known_primes = [2, 3]

    def save_known_primes_file(self):
        bkp_data = self.u.lod("assets/bigprime.pickle")
        if bkp_data != self.known_primes:
            self.u.sav(bkp_data, "assets/bigprime.pickle.bak")
            self.u.sav(self.known_primes, "assets/bigprime.pickle")
            print("saved")

    def is_prime(self, x, starting_val=5):
        for y in self.known_primes:
            if x % y == 0:
                return False
        for y in range(starting_val, x - 1, 2):
            if x % y == 0:
                return False
        self.known_primes.append(x)
        return True

    def is_prime_turbo(self, x):
        return self.is_prime(x, starting_val=self.known_primes[-1])


class utility:
    def __init__(self):
        pass

    def tstart(self):
        self.tick = time.perf_counter()

    def tstop(self):
        ptime = time.perf_counter() - self.tick
        print("processing_time: {0:.6g} s".format(ptime))

    def sav(self, d, savefile):
        with open(savefile, "wb") as outfile:
            pickle.dump(d, outfile)

    def lod(self, savefile):
        with open(savefile, "rb") as infile:
            d = pickle.load(infile)
        return d


if __name__ == "__main__":
    pass
