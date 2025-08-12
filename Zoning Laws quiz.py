import tkinter as tk
import random

# Format: (Question, [Choices], Correct Answer, Short Praise, Long Explanation)
all_questions = [
    ("What does NX-5 mean?",
     ["Neighborhood Mixed Use, 5-story max", "Neighborhood X, zone 5", "Next Exit 5", "Mixed Neighborhood Zone"],
     "Neighborhood Mixed Use, 5-story max", "✅ NX zones allow housing + light commercial up to 5 stories. 🏘️", "NX zones allow both housing and light commercial—capped at five stories."),

    ("If a lot is zoned DX-12-SH, what’s required on the ground floor?",
     ["Shopfront", "Parking", "Apartment entrance", "Garage"],
     "Shopfront", "✅ SH = shopfront required at street level. 🛍️", "SH means ground-floor retail is required for walkability."),

    ("What does a -PK suffix mean in zoning?",
     ["Parkway", "Parking", "Parcel", "Peak"],
     "Parkway", "✅ PK zones require buildings to be set back with landscaping. 🌳", "PK zones require buildings to sit back with landscaped buffers."),

    ("What zone allows residential and retail downtown?",
     ["DX", "NX", "RX", "CX"],
     "DX", "✅ DX = flexible, dense downtown zoning. 🏢", "DX zones enable dense, flexible downtown development."),

    ("What is a variance?",
     ["Permission to break a rule", "Permission to sell", "Building permit", "Rent agreement"],
     "Permission to break a rule", "✅ A variance allows legal exceptions to zoning rules. 📜", "It’s a city-approved exception to zoning rules."),

    ("What is an entitlement in development?",
     ["Approval to build", "Sales approval", "Utility billing", "Survey completion"],
     "Approval to build", "✅ Entitlement = permission from the city to build something specific. 🏗️", "Entitlement is permission from the city to construct something specific."),

    ("What is an RFP (Request for Proposal)?",
     ["A call to submit project ideas for a site", "A zoning code", "An application for utilities", "A legal dispute form"],
     "A call to submit project ideas for a site", "✅ RFPs say: 'Send us your design and plan.' 📑", "An RFP is a formal document from a city/company saying: 'We have land — send us your plan to build on it.'"),

    ("What is an RFQ (Request for Qualifications)?",
     ["A résumé-like submission before an RFP", "Zoning appeal form", "Permit request", "Cost reimbursement"],
     "A résumé-like submission before an RFP", "✅ RFQs ask for your experience and credentials. 🧑‍💼", "An RFQ asks: 'Tell us why you’re qualified.' Often comes before an RFP."),

    ("What’s a TOD (Transit-Oriented Development)?",
     ["A building near transit stops", "A zoning code for farmland", "A type of shopping center", "A parking tax zone"],
     "A building near transit stops", "✅ TOD = denser buildings near train/bus stops. 🚉", "TODs are built near transit to reduce car use and increase walkability."),

    ("How much does it cost to build an apartment per unit (basic)?",
     ["$150k–$180k", "$90k–$100k", "$300k–$350k", "$50k–$80k"],
     "$150k–$180k", "✅ ~$150k–$180k for affordable/basic units in Raleigh. 🏗️", "That’s the rough range for affordable unit construction including fees and land."),

    ("What are soft vs. hard costs?",
     ["Soft = design/legal, Hard = materials/labor", "Soft = heating, Hard = rent", "Soft = monthly bills, Hard = yearly tax", "Soft = finishings, Hard = blueprint cost"],
     "Soft = design/legal, Hard = materials/labor", "✅ Hard = physical build. Soft = permits, legal, design. 📊", "Hard = building materials/labor. Soft = permits, architect fees, insurance."),

    ("What is a pro forma?",
     ["A financial projection for a project", "Permit for demolition", "Blueprint design", "Environmental cleanup plan"],
     "A financial projection for a project", "✅ Pro forma = rent, costs, profit, all in one. 💰", "Pro formas help investors/lenders understand your project’s financials."),

    ("What is infill development?",
     ["Building on small empty lots in existing areas", "Expanding into farmland", "Demolishing city blocks", "Building malls near highways"],
     "Building on small empty lots in existing areas", "✅ Infill = smart growth on leftover city land. 🧱", "Infill builds new housing without sprawl, often in underused urban lots."),

    ("What is inclusionary zoning?",
     ["Requiring some affordable units", "Zoning near schools", "A ban on short-term rentals", "Extra taxes on high rises"],
     "Requiring some affordable units", "✅ Developers must include low-income units. 🏠", "It mandates that a portion of new housing be affordable."),

    ("What is land assemblage?",
     ["Buying multiple small lots to make one big one", "Donating land to the city", "Farming unused land", "Turning lots into parking"],
     "Buying multiple small lots to make one big one", "✅ Assemble land = build bigger projects. 📦", "Developers use land assemblage to create larger buildable lots."),

    ("What is a JV (Joint Venture)?",
     ["Two+ groups team up to do a deal", "A zoning violation", "A federal loan program", "A public park initiative"],
     "Two+ groups team up to do a deal", "✅ JV = shared deal, shared risk, shared reward. 🤝", "One party might own the land, another funds it—they split profit."),

    ("What’s a brownfield site?",
     ["Possibly polluted land from old use", "Farmland in suburbs", "Vacant retail", "Land owned by banks"],
     "Possibly polluted land from old use", "✅ Brownfields = cleanup before reuse. ☣️", "Brownfields are former industrial/gas sites needing environmental review."),

    ("What’s a developer fee?",
     ["Payment to the developer to manage the project", "Permit cost", "Legal fine", "Loan fee"],
     "Payment to the developer to manage the project", "✅ Developers get paid for overseeing everything. 💼", "Developer fees (usually 5–10%) cover managing the deal start to finish.")
]

class QuizGame:
    def __init__(self, master):
        self.master = master
        master.title("Zoning & Development Quiz")
        master.geometry("780x480")
        master.configure(bg="#f9b7bd")
        self.setup_widgets()
        self.reset_quiz()

    def setup_widgets(self):
        self.question_label = tk.Label(self.master, text="", wraplength=700, font=("Arial", 14), fg="#fff44f", bg="#f9b7bd")
        self.question_label.pack(pady=10)

        self.choices_frame = tk.Frame(self.master, bg="#f9b7bd")
        self.choices_frame.pack()

        self.submit_btn = tk.Button(self.master, text="Submit Answer", command=self.check_answer, bg="#eeeeee", fg="#fff44f")
        self.submit_btn.pack(pady=5)

        self.feedback_label = tk.Label(self.master, text="", font=("Arial", 12), bg="#f9b7bd")
        self.feedback_label.pack(pady=5)

        self.correct_label = tk.Label(self.master, text="", font=("Arial", 12), fg="#006400", bg="#ccffcc")
        self.explanation_label = tk.Label(self.master, text="", wraplength=650, font=("Arial", 11), fg="#006400", bg="#ccffcc")

        self.next_btn = tk.Button(self.master, text="Next Question", command=self.next_question, bg="#eeeeee", fg="#fff44f")
        self.next_btn.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 14, "bold"), fg="#fff44f", bg="#f9b7bd")
        self.result_label.pack(pady=10)

        self.retry_btn = tk.Button(self.master, text="Play Again", command=self.reset_quiz, bg="#eeeeee", fg="#fff44f")

    def reset_quiz(self):
        self.questions = random.sample(all_questions, 10)
        self.q_index = 0
        self.score = 0
        self.incorrect_answers = []
        self.result_label.config(text="")
        self.feedback_label.config(text="")
        self.correct_label.pack_forget()
        self.explanation_label.pack_forget()
        self.retry_btn.pack_forget()
        self.choices_frame.pack()
        self.submit_btn.pack()
        self.next_btn.pack()

        # Destroy and recreate radio buttons
        for btn in getattr(self, 'choice_buttons', []):
            btn.destroy()
        self.choice_buttons = []
        self.selected_option = tk.StringVar()
        for _ in range(4):
            btn = tk.Radiobutton(self.choices_frame, text="", variable=self.selected_option, value="",
                                 font=("Arial", 12), fg="#fff44f", bg="#f9b7bd", selectcolor="#eeeeee")
            btn.pack(anchor="w")
            self.choice_buttons.append(btn)

        self.next_question()

    def check_answer(self):
        q, choices, correct, short_exp, long_exp = self.questions[self.q_index - 1]
        user_input = self.selected_option.get()
        if user_input == correct:
            self.feedback_label.config(text=short_exp, fg="#006400", bg="#ccffcc")
            self.correct_label.pack_forget()
            self.explanation_label.pack_forget()
            self.score += 1
        else:
            self.feedback_label.config(text="❌ Incorrect.", fg="#fff44f", bg="#f9b7bd")
            self.correct_label.config(text=f"✔️ Correct answer: {correct}")
            self.explanation_label.config(text=f"📝 {long_exp}")
            self.correct_label.pack(pady=3)
            self.explanation_label.pack(pady=3)
            self.incorrect_answers.append((q, correct, long_exp))
        self.submit_btn.config(state=tk.DISABLED)

    def next_question(self):
        if self.q_index < len(self.questions):
            q, choices, correct, short_exp, long_exp = self.questions[self.q_index]
            self.question_label.config(text=f"Q{self.q_index + 1}: {q}")
            self.feedback_label.config(text="")
            self.correct_label.pack_forget()
            self.explanation_label.pack_forget()
            self.submit_btn.config(state=tk.NORMAL)

            self.selected_option.set("")
            for i, btn in enumerate(self.choice_buttons):
                if i < len(choices):
                    btn.config(text=choices[i], value=choices[i])
                    btn.pack()
                else:
                    btn.pack_forget()

            self.q_index += 1
        else:
            self.show_results()

    def show_results(self):
        self.question_label.config(text="🏁 Quiz Complete!")
        self.choices_frame.pack_forget()
        self.submit_btn.pack_forget()
        self.next_btn.pack_forget()
        self.feedback_label.pack_forget()
        self.correct_label.pack_forget()
        self.explanation_label.pack_forget()

        self.result_label.config(text=f"You scored {self.score} out of {len(self.questions)}!\n")
        if self.incorrect_answers:
            missed = "Here’s what you missed:\n"
            for q, correct, explanation in self.incorrect_answers:
                missed += f"\n❌ {q}\n✔️ Correct: {correct}\n📝 {explanation}\n"
            self.result_label.config(text=self.result_label.cget("text") + missed)

        self.retry_btn.pack()

root = tk.Tk()
quiz = QuizGame(root)
root.mainloop()
