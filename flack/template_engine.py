from jinja2 import Environment, FileSystemLoader


class Engine:
    def __init__(self, template_paths: str = ''):
        self.engine = Environment(loader=FileSystemLoader(searchpath=template_paths))

    def render(self, template_name: str, **kwargs) -> str:
        template = self.engine.get_template(template_name)
        return template.render(**kwargs['context'])