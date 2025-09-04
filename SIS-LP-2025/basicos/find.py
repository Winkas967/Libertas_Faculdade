texto = "      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer turpis urna, ultrices in quam eu, pellentesque consectetur risus. Etiam a dolor id quam porttitor posuere. Nunc sagittis interdum nisl a dapibus. Pellentesque vulputate dapibus lorem, quis fermentum quam pellentesque sed. Pellentesque leo justo, molestie non enim ut, sodales ullamcorper dolor. Integer turpis odio, pretium et dolor id, consectetur fringilla leo. Cras nec est quis lorem pharetra tempor id eu mauris. Phasellus et porttitor velit. Aliquam feugiat nulla tempus orci fermentum auctor. Proin convallis, sapien nec feugiat accumsan, nisi magna bibendum velit, eget aliquam mauris lorem et enim. Aenean quis lacus fermentum, interdum velit molestie, ornare nibh.      "

ind = texto.find("a")
print(ind)
comprimento = len(texto)
ind = -10
while ind !=-10:
    if ind !=10:
        ind = texto.find("a", ind+1, comprimento)
    else: 
        ind = texto.find("a")
        
    print(f"indices {ind}")
    
print(texto)

texto = texto.strip()  # remove os espaços da frase
print("-" * 50)
print(texto)