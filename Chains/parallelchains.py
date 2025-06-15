from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)
model2=ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template='Generate short and simple notes from the following text. \n {text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='Generate 5 short questions and answers from following text. \n {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='Merge the provided notes and quiz into a single document. \n notes->{notes} and quiz->{quiz}',
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parallelchain=RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model2 | parser
})

mergerchain= prompt3 | model |  parser

chain= parallelchain | mergerchain

txt="Black holes are among the most fascinating and mysterious objects in the universe. Formed when massive stars collapse under their own gravity after exhausting their nuclear fuel, black holes represent regions in space where gravity is so intense that nothing—not even light—can escape their pull. The boundary surrounding a black hole is known as the event horizon, and once something crosses it, there's no return.Black holes come in various sizes. Stellar black holes, which form from collapsing stars, typically have a mass several times that of our Sun. Supermassive black holes, on the other hand, are millions or even billions of times more massive and are found at the centers of most galaxies, including our own Milky Way. Scientists believe these giants may play a crucial role in galaxy formation and evolution.Despite their dark nature, black holes can be detected indirectly. As they draw in surrounding matter, the material forms an accretion disk and heats up, emitting X-rays and other radiation that can be observed with telescopes. Some black holes also emit powerful jets of particles at near-light speeds, making them visible across vast distances.In recent years, major scientific breakthroughs have advanced our understanding of black holes. In 2019, the Event Horizon Telescope captured the first image of a black hole's shadow in the galaxy M87—a milestone in astrophysics. Moreover, gravitational wave detectors like LIGO and Virgo have recorded the ripples in spacetime caused by black hole mergers.Black holes challenge our understanding of physics, particularly where general relativity and quantum mechanics intersect. At their core lies a singularity—a point of infinite density—where known laws of physics break down. Studying black holes not only deepens our knowledge of the universe but may also unlock answers to fundamental questions about space, time, and the nature of reality itself."
result= chain.invoke({'text':txt})

print(result)