import openai
openai.api_key = ""

class IAAlRescate:
    def __init__(self, api_key):
        """
        Inicializa la clase con la clave API.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def generar_respuesta_texto(self, prompt, model="gpt-4o-mini", max_tokens=200, temperature=0.7):
        """
        Genera una respuesta de texto a texto basada en el prompt.
        """
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Eres un asistente que resuelve problemas humanos."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response['choices'][0]['message']['content']
        except openai.error.OpenAIError as e:
            return f"Error al generar texto: {e}"

    def generar_respuesta_imagen(self, prompt, model="dalle-mini"):
        """
        Genera una imagen basada en un prompt.
        """
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            return response['data'][0]['url']
        except openai.error.OpenAIError as e:
            return f"Error al generar imagen: {e}"

    def evaluar_respuesta(self, respuesta, criterios=["Eficiencia", "Relevancia", "Claridad"]):
        """
        Evalúa una respuesta de texto basada en criterios.
        """
        evaluacion = {criterio: "Pendiente" for criterio in criterios}
        return evaluacion

    def asistencia_tecnica_codigo(self, problema_codigo, lenguaje="Python"):
        """Genera una respuesta para resolver problemas técnicos de código en un lenguaje específico."""
        prompt = f"Soy un desarrollador que no entiende {lenguaje}. Aquí está el problema que enfrento: '{problema_codigo}'. ¿Cómo puedo resolverlo?"
        try:
            respuesta = self.generar_respuesta_texto(prompt, model="gpt-4")
            return respuesta
        except openai.error.OpenAIError as e:
            return f"Error al procesar el problema de código: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    api_key = "" 
    ia_rescate = IAAlRescate(api_key)

    # Ejemplo 1: Texto a texto
    prompt_texto = "Diseña un horario detallado priorizando las tareas más importantes de mi día, teniendo en cuenta que trabajo 8 horas."
    respuesta_texto = ia_rescate.generar_respuesta_texto(prompt_texto)
    print("Respuesta de Texto a Texto:\n", respuesta_texto)

    # Ejemplo 2: Texto a imagen
    prompt_imagen = "Genera una imagen de un jardín zen al atardecer, con un estanque, piedras organizadas y bambú rodeándolo."
    respuesta_imagen = ia_rescate.generar_respuesta_imagen(prompt_imagen)
    print("URL de la Imagen Generada:\n", respuesta_imagen)

    # Ejemplo 3: Evaluación de una respuesta
    evaluacion = ia_rescate.evaluar_respuesta(respuesta_texto)
    print("Evaluación de la Respuesta:\n", evaluacion)

    # Ejemplo 4: Asistencia técnica para problemas de código
    problema = "Tengo un error de sintaxis en mi código Python cuando intento definir una función."
    respuesta_tecnica = ia_rescate.asistencia_tecnica_codigo(problema, "Python")
    print("Respuesta para Asistencia Técnica:", respuesta_tecnica)


print(dir(IAAlRescate))