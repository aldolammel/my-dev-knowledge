
# DJANGO-POLYMORPHIC: BASIC EXAMPLES
# This is basically all you need to know, as django-polymorphic mostly works fully automatic and just delivers the expected results.


# BUILDING POLYMORPHIC MODELS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# All models inheriting from your polymorphic models will be polymorphic as well.

from polymorphic.models import PolymorphicModel

class Project(PolymorphicModel):
    topic = models.CharField(max_length=30)

class ArtProject(Project):
    artist = models.CharField(max_length=30)

class ResearchProject(Project):
    supervisor = models.CharField(max_length=30)



# IN ADMIN - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Check this example: ./real-case.py



# CREATING SOME OBJS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Project.objects.create(topic="Department Party")
ArtProject.objects.create(topic="Painting with Tim", artist="T. Turner")
ResearchProject.objects.create(topic="Swallow Aerodynamics", supervisor="Dr. Winter")




# GETTING POLYMORPHIC QUERY RESULTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Project.objects.all()

"""[ <Project:         id 1, topic "Department Party">,
     <ArtProject:      id 2, topic "Painting with Tim", artist "T. Turner">,
     <ResearchProject: id 3, topic "Swallow Aerodynamics", supervisor "Dr. Winter"> ]"""



# NARROWING THE RESULT TO SPECIFIC SUBTYPES - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Using instance_of()
Project.objects.instance_of(ArtProject) | Project.objects.instance_of(ResearchProject)
"""[ <ArtProject:      id 2, topic "Painting with Tim", artist "T. Turner">,
     <ResearchProject: id 3, topic "Swallow Aerodynamics", supervisor "Dr. Winter"> ]"""

# Using not_instance_of()





# FILTERING - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Project.objects.filter(Q(ArtProject___artist='T. Turner') | Q(ResearchProject___supervisor='T. Turner'))
"""[ <ArtProject:      id 2, topic "Painting with Tim", artist "T. Turner">,
     <ResearchProject: id 4, topic "Color Use in Late Cubism", supervisor "T. Turner"> ]"""