import numpy as np
import matplotlib.pyplot as plt

class Kolam(object):

    def __init__(self):
        self.radius = 0.25
        self.position = np.array([0., 0.])
        self.direction = np.array([1., 0.])
        plt.axis("off")
        return

    def _go_one_unit(self):
        newposition = self.position + self.direction
        plt.plot([self.position[0], newposition[0]], [self.position[1], newposition[1]], 'k')
        self.position = newposition
        return
        
    def _turn_90(self):
        newposition1 = self.position + self.radius * self.direction
        newdirection = np.dot(np.array([[0., 1.], [-1., 0.]]), self.direction)
        newposition2 = newposition1 + self.radius * newdirection
        plt.plot([self.position[0], newposition1[0], newposition2[0]],
                 [self.position[1], newposition1[1], newposition2[1]], 'k')
        self.direction = newdirection
        self.position = newposition2
        return

    def _turn_270(self):
        self._turn_90()
        self._turn_90()
        return self._turn_90()

    def _step_90(self):
        self._go_one_unit()
        return self._turn_90()

    def _step_270(self):
        self._go_one_unit()
        return self._turn_270()

    def draw2(self, fn):
        for i in range(4):
            self._step_270()
        plt.axis("equal")
        print "writing %s" % fn
        return plt.savefig(fn)

    def draw4(self, fn):
        for i in range(4):
            for j in range(3):
                self._step_270()
            for j in range(2):
                self._step_90()
        plt.axis("equal")
        print "writing %s" % fn
        return plt.savefig(fn)

    def draw4(self, fn):
        for i in range(4):
            for j in range(3):
                self._step_270()
            for j in range(2):
                self._step_90()
        plt.axis("equal")
        print "writing %s" % fn
        return plt.savefig(fn)

    def draw8(self, fn):
        for h in range(4):
            self._step_270()
            self._step_90()
            self._step_90()
            for i in range(3):
                for j in range(3):
                    self._step_270()
                for j in range(2):
                    self._step_90()
            self._step_270()
            self._step_90()
            self._step_90()
        plt.axis("equal")
        print "writing %s" % fn
        return plt.savefig(fn)

if __name__ == "__main__":
    k = Kolam()
    k.draw2("k2.pdf")
    k.draw4("k4.pdf")
    k.draw8("k8.pdf")
