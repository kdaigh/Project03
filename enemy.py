from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class Enemy(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

    # def add_enemy():
    # add groups of enemies
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.0025, 0.0025, 0.0025)
        self.pandaActor.loop("walk")
        self.pandaActor.reparentTo(self.render)

        for j in range (17):
            for i in range (18):
                self.placeholder = self.render.attachNewNode("panda")
                self.placeholder.setPos(-9+(i*2),20,4)
                self.pandaActor.instanceTo(self.placeholder)
            #self.placeholder2 = self.render.attachNewNode("panda")
            self.placeholder.setPos(-11+(j*2),20,0)
            self.pandaActor.instanceTo(self.placeholder)

        pandaPosInterval1 = self.pandaActor.posInterval(7,
                                                        Point3(0, 20, 4),
                                                        startPos=Point3(-9,20, 4))
        pandaPosInterval2 = self.pandaActor.posInterval(7,
                                                        Point3(0, 20, 0),
                                                        startPos=Point3(0, 20, 4))
        pandaPosInterval3 = self.pandaActor.posInterval(7,
                                                        Point3(-9, 20, 4),
                                                        startPos=Point3(0, 20, 0))
            #pandaHprInterval1 = self.pandaActor.hprInterval(3,
            #                                                Point3(180, 0, 0),
            #                                                startHpr=Point3(0, 0, 0))
            #pandaHprInterval2 = self.pandaActor.hprInterval(3,
            #                                                Point3(0, 0, 0),
            #                                                startHpr=Point3(180, 0, 0))


            # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(pandaPosInterval1,
        #                          pandaHprInterval1,
                                  pandaPosInterval2,
        #                          pandaHprInterval2,
                                  pandaPosInterval3,
                                  name="pandaPace")
        self.pandaPace.loop()


        # Loop its animation.
