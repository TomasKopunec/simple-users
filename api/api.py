from api.samples.a import function_a
from api.samples.b import function_b
from api.samples.layers.c import function_c


class Api():
    def run():
        function_a()
        function_b()

    def process():
        print("Processing data...")
        function_c()
        
def main():
    Api.run()
    Api.process()
