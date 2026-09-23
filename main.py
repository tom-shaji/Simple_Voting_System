def main():
    # List of 4 candidates
    candidates = ["Alice", "Bob", "Charlie", "David"]
    
    # Store votes using a Python dictionary
    votes = {candidate: 0 for candidate in candidates}
    
    # Keep track of who has voted to prevent duplicate voting
    voters = set()
    
    while True:
        print("\n--- Voting System Menu ---")
        print("1. Cast Vote")
        print("2. View Vote Count")
        print("3. View Voting Results")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            name = input("Enter your name: ").strip()
            
            if not name:
                print("Name cannot be empty.")
                continue
            
            # Check for duplicate voter names (case-insensitive)
            if name.lower() in [v.lower() for v in voters]:
                print(f"Sorry, {name}. You have already voted!")
                continue
                
            print("\nCandidates:")
            for idx, candidate in enumerate(candidates, 1):
                print(f"{idx}. {candidate}")
                
            try:
                candidate_choice = int(input("Select a candidate by number: "))
                
                # Handle invalid candidate choices
                if 1 <= candidate_choice <= len(candidates):
                    selected_candidate = candidates[candidate_choice - 1]
                    votes[selected_candidate] += 1
                    voters.add(name)
                    print(f"\nThank you, {name}! Your vote for {selected_candidate} has been recorded.")
                else:
                    print("\nInvalid candidate choice. Please select a valid number.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                
        elif choice == '2':
            print("\n--- Current Vote Count ---")
            for candidate, count in votes.items():
                print(f"{candidate}: {count} votes")
            print(f"\nTotal number of voters: {len(voters)}")
            
        elif choice == '3':
            print("\n--- Final Voting Results ---")
            for candidate, count in votes.items():
                print(f"{candidate}: {count} votes")
                
            print(f"\nTotal number of voters: {len(voters)}")
            
            if len(voters) == 0:
                print("No votes have been cast yet.")
            else:
                # Find the maximum number of votes
                max_votes = max(votes.values())
                
                # Find the candidate(s) with the maximum votes
                winners = [candidate for candidate, count in votes.items() if count == max_votes]
                
                if len(winners) == 1:
                    print(f"\nThe winner is {winners[0]} with {max_votes} votes!")
                else:
                    print(f"\nIt's a tie! The winners are {', '.join(winners)} with {max_votes} votes each.")
                    
        elif choice == '4':
            print("\nExiting Voting System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
