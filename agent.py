import ollama
import software_a
import software_b
import software_c


MODEL = "gemma4:31b-cloud"


def ask_ollama(number, iteration):
    prompt = f"""You are controlling 3 software tools that operate on numbers.

The tools are:
- software_a : doubles the number  (good when number is small, under 20)
- software_b : subtracts 3         (good when number is large, over 50)
- software_c : finds square root   (good when number is between 20 and 50)

Current number : {number}
Iteration      : {iteration} out of 10

Your job:
1. Pick the best tool to call RIGHT NOW based on the current number.
2. If iteration has reached 10, you MUST reply with: stop

Reply with ONLY one of these four words:
software_a
software_b
software_c
stop

No explanation. No punctuation. Just one word."""

    response = ollama.chat(
        model="gemma4:31b-cloud",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0, "num_predict": 10}
    )

    reply = response["message"]["content"].strip().lower()
    reply = reply.split()[0].replace(".", "").replace(",", "")
    return reply

print("welcome to the AI number Agent!")
print("Powered by Ollama and Gemma")
def run_agent():
    number = int(input("Enter a starting number: "))
    iteration = 0

    
    print(f"  Model        : {MODEL}")
    print(f"  Start number : {number}")
    print(f"  Max loops    : 10 (AI decides when to stop)")
    print("="*45)

    while True:
        iteration += 1
        print(f"\n Iteration {iteration} | Current number: {number} ")

        decision = ask_ollama(number, iteration)
        print(f"  [Ollama - {MODEL}] Decision: {decision}")

        if decision == "stop":
        
            print(f"  AI decided to STOP at iteration {iteration}.")
            print(f"  Final number: {number}")
            
            break
        elif decision == "software_a":
            number = software_a.run(number)
        elif decision == "software_b":
            number = software_b.run(number)
        elif decision == "software_c":
            number = software_c.run(number)
        else:
            print(f"  [Agent] Unexpected reply '{decision}', stopping.")
            break

    print("\nDone! Run again: python agent.py")


print("now you understand the Agent")
print("talk you again")
if __name__ == "__main__":
    run_agent()
