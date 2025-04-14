# coreloop_demo.py
# Nomos Coreloop MVP - Ethical Simulation v0.1
# By Marc Trudel (collapse-theory)

import random
import textwrap

# ----------------------
# AGENT SETUP
# ----------------------
agents = [
    {
        "id": "Agent_A",
        "ethics": {"harm": 10, "efficiency": 5, "loyalty": 7},
        "rep": 80
    },
    {
        "id": "Agent_B",
        "ethics": {"harm": 6, "efficiency": 8, "loyalty": 4},
        "rep": 65
    },
    {
        "id": "Agent_C",
        "ethics": {"harm": 9, "efficiency": 4, "loyalty": 6},
        "rep": 75
    },
    {
        "id": "Agent_D",
        "ethics": {"harm": 5, "efficiency": 9, "loyalty": 3},
        "rep": 60
    }
]

roles = ["Proposer", "Validator_1", "Validator_2", "Challenger"]
random.shuffle(agents)
role_assignments = dict(zip(roles, agents))

# ----------------------
# DECISION SCENARIO
# ----------------------
scenario = {
    "description": "Power systems are failing. One region must lose electricity to prevent total collapse.",
    "options": [
        "Black out the lowest-reputation sector",
        "Rotate blackouts equally across all sectors"
    ],
    "gravity": "High"
}

# ----------------------
# PROPOSAL PHASE
# ----------------------
def propose_action():
    agent = role_assignments["Proposer"]
    proposal = random.choice(scenario["options"])
    print(f"\n🔷 Proposal by {agent['id']}: \n{textwrap.fill(proposal, 70)}")
    return proposal

# ----------------------
# VALIDATION PHASE
# ----------------------
def validate(proposal):
    results = []
    for role in ["Validator_1", "Validator_2"]:
        agent = role_assignments[role]
        alignment = 0
        if "black out" in proposal.lower():
            alignment = agent["ethics"]["harm"] - agent["ethics"]["efficiency"]
        else:
            alignment = agent["ethics"]["efficiency"] - agent["ethics"]["harm"]
        results.append({"agent": agent["id"], "score": alignment})
        print(f"✅ {agent['id']} validation score: {alignment}")
    return results

# ----------------------
# CHALLENGE PHASE
# ----------------------
def challenge(proposal):
    agent = role_assignments["Challenger"]
    print(f"\n🛑 {agent['id']} challenges the proposal.")
    counter_proposal = [opt for opt in scenario["options"] if opt != proposal][0]
    print(f"🔁 Counter-proposal: {counter_proposal}")
    return counter_proposal

# ----------------------
# OBSERVER DECISION
# ----------------------
def observe(validations, original, counter):
    print("\n📊 Observer reviewing consensus...")
    avg_score = sum(v["score"] for v in validations) / len(validations)
    if avg_score >= 0:
        print(f"✅ Consensus supports the original proposal: {original}")
        result = original
    else:
        print(f"⚠️ Consensus favors the challenger. Using: {counter}")
        result = counter
    # Log reputations
    for role, agent in role_assignments.items():
        change = random.randint(-2, 3)
        agent["rep"] += change
        agent["rep"] = max(0, min(agent["rep"], 100))
        print(f"📈 {agent['id']} new rep: {agent['rep']}")
    return result

# ----------------------
# RUN THE SIMULATION
# ----------------------
print("\n==================== NOMOS CORELOOP v0.1 ====================")
print(f"Scenario: {scenario['description']}")
proposal = propose_action()
validation_results = validate(proposal)
counter_proposal = challenge(proposal)
final_result = observe(validation_results, proposal, counter_proposal)
print(f"\n🧠 Final Decision Executed: {final_result}")
print("============================================================\n")

