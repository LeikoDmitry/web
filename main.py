import os
from flack.main import Flack
from urls import urlpatterns


if __name__ == '__main__':
    options = {
        'bind': '{0}:{1}'.format('0.0.0.0', 8090),
        'workers': Flack.number_of_workers(),
        'urls': urlpatterns,
        'base_dir': os.path.dirname(os.path.abspath(__file__)),
        'templates_dir_name': 'templates'
    }
    app = Flack(options=options)
    app.run()
