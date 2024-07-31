class valo_aim_trainer:
    def aim_trainer():
        rank = input("Enter your rank in lower case perfectly: ")
        if rank == 'platinum' or 'diamond' or 'ascendant' or 'immortal' or 'radiant':
            msg_high = '''Aim and Practice Routine for High-Rank Players (Platinum+)
                    Focus: Refinement, consistency, and adaptability.

                    Warm-up (15-20 minutes):
                    Static crosshair placement: Practice holding your crosshair on specific points on the screen for extended periods.
                    Tracking drills: Follow moving targets at various speeds and angles.
                    Flick shots: Train rapid target acquisition and precision.
                    Aim training (30-45 minutes):
                    Aim Labs or Kovaak's: Utilize custom scenarios to target specific weaknesses (e.g., flicking, tracking, micro-adjustments).
                    Deathmatch: Practice aim in a live environment, focusing on crosshair placement, recoil control, and shot accuracy.
                    Agent-specific practice (15-20 minutes):
                    Master ability usage: Experiment with different scenarios and combinations.
                    Line-up practice: Perfect ability placements for optimal impact.
                    Competitive matches (1-2 hours):
                    Apply skills in-game: Focus on decision-making, map awareness, and teamwork.
                    Analyze gameplay: Review demos to identify areas for improvement.
                    Additional Tips:

                    Consistency: Practice regularly, even if it's for short durations.
                    Variety: Incorporate different aim training exercises to prevent plateaus.
                    Mental game: Develop strategies to manage stress and maintain focus.
                    Teamwork: Communicate effectively and coordinate with your team.'''
            


            aim_labs_tranings_high ='''  High-Rank Players (Platinum+)
                                    Focus: Precision, reaction time, and adaptability.

                                    Warm-up:
                                    Straight Shot: Improve consistency and click accuracy.
                                    Target Switch: Enhance target acquisition and flicking.
                                    Main Course:
                                    Flick Shot: Develop rapid target acquisition and precision.
                                    Tracking: Improve ability to follow moving targets at various speeds.
                                    Reaction Time: Enhance response time to sudden targets.
                                    Strafe Shot: Practice shooting while moving.
                                    Cooldown:
                                    Aim Hero: Identify strengths and weaknesses.
                                    Gridshot: Improve crosshair placement and consistency. '''


            print(msg_high)
            usr_chs = input("Do you want to see which aimlabs traning you should use y/n: ")
            if usr_chs == 'y':
                print(aim_labs_tranings_high)
            elif usr_chs == 'n':
                print('bye')
            else:
                print("Error")

                
        elif rank == 'iron' or 'bronze' or 'silver' or 'gold':
            msg_low = '''   Aim and Practice Routine for Low-Rank Players (Iron-Gold)
                        Focus: Fundamentals, consistency, and muscle memory.

                        Warm-up (10-15 minutes):
                        Static crosshair placement: Build muscle memory for accurate aiming.
                        Basic tracking drills: Improve ability to follow targets.
                        Aim training (20-30 minutes):
                        Aim Labs or Kovaak's: Start with basic scenarios to establish foundations.
                        Deathmatch: Practice gunplay and movement mechanics.
                        Game sense (15-20 minutes):
                        Watch pro players or streamers: Learn map control, economy management, and team coordination.
                        Observe your gameplay: Identify common mistakes and areas for improvement.
                        Competitive matches (1-2 hours):
                        Apply what you've learned: Focus on basic mechanics and decision-making.
                        Communicate with your team: Build trust and improve coordination.
                        Additional Tips:

                        Patience: Improvement takes time. Avoid getting discouraged.
                        Fundamentals: Master basic mechanics before moving to advanced techniques.
                        Game sense: Understanding the game is as important as aim.
                        Positive attitude: A good mindset can significantly impact performance.'''
            

            aim_labs_tranings_low ='''  Low-Rank Players (Iron-Gold)
                                    Focus: Fundamentals, consistency, and muscle memory.

                                    Warm-up:
                                    Straight Shot: Build basic accuracy and consistency.
                                    Tracking (slow): Start with slower targets to build muscle memory.
                                    Main Course:
                                    Click Test: Improve click speed and accuracy.
                                    Target Switch (easy): Develop basic flicking ability.
                                    Tracking (medium): Gradually increase target speed.
                                    Strafe Shot (slow): Practice shooting while moving at a controlled pace.
                                    Cooldown:
                                    Aim Hero: Identify areas for improvement.
                                    Gridshot: Develop basic crosshair placement. '''
            print(msg_low)
            usr_chs = int(input("Do you want to see which aimlabs traning you should use y/n: "))
            if usr_chs == 'y':
                print(aim_labs_tranings_low)
            elif usr_chs == 'n':
                print('bye')
            else:
                print("Error")
        else:
            print("Error")


if __name__ == '__main__':
    vat = valo_aim_trainer
    vat.aim_trainer()