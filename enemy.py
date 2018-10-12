from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class Enemy(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

    #def add_enemy():

        # Load and transform the panda actor.

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.001, 0.001, 0.001)
        #self.pandaActor.setPos(-9,20,4)
        self.pandaActor.loop("walk")
        self.pandaActor.reparentTo(self.render)
        for j in range (10):
            for i in range (10):
                self.placeholder = self.render.attachNewNode("panda")
                self.placeholder.setPos(-9+(i*2),20,4)
                self.pandaActor.instanceTo(self.placeholder)
            self.placeholder2 = self.render.attachNewNode("panda")
            self.placeholder2.setPos(-8+(j*2),20,2)
            self.pandaActor.instanceTo(self.placeholder2)
            pandaPosInterval1 = self.pandaActor.posInterval(10,
                                                            Point3(-5, 10, 0),
                                                            startPos=Point3(0, 10, 0))
            pandaPosInterval2 = self.pandaActor.posInterval(10,
                                                            Point3(5, 10, 0),
                                                            startPos=Point3(0, 10, 0))
            pandaHprInterval1 = self.pandaActor.hprInterval(3,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval2 = self.pandaActor.hprInterval(3,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))


            # Create and play the sequence that coordinates the intervals.
            self.pandaPace = Sequence(pandaPosInterval1,
                                      pandaHprInterval1,
                                      pandaPosInterval2,
                                      pandaHprInterval2,
                                      name="pandaPace")
            self.pandaPace.loop()
        # Loop its animation.


app = Enemy()
# run should be called once at the end, I am using it here just for testing purposes.
app.run()
