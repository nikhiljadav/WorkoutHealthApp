def calculate_recommended_weight(exercise):
    # Set the base weight increment based on exercise type
    base_increment = 5 if exercise.type == 'compound' else 2.5

    # Initialize recWeight if it is None
    if exercise.recWeight is None:
        exercise.recWeight = 0

    # Get the lower and upper rep range limits
    lower_range = exercise.lowerRange
    upper_range = exercise.upperRange

    # Initialize variables to track performance across sets
    total_reps = 0
    total_sets = 0
    high_rpe_count = 0
    highest_weight = 0

    # Iterate through all sets associated with the exercise
    for set_obj in exercise.sets.all():
        total_reps += set_obj.reps
        total_sets += 1
        if set_obj.weight > highest_weight:
            highest_weight = set_obj.weight
        if set_obj.RPE >= 8:  # Consider RPE 8 or above as "high"
            high_rpe_count += 1

    # Calculate average reps per set
    average_reps = total_reps / total_sets if total_sets > 0 else 0

    # Calculate the recommended action based on performance
    if average_reps > upper_range + 5 and high_rpe_count < total_sets * 0.5:
        # Significant increase if reps far exceed the upper range with low RPE
        weight_increase = base_increment * 3
        recommendation = f"Increase weight by {weight_increase} lbs"
    elif average_reps > upper_range:
        # Moderate increase if reps exceed the upper range
        weight_increase = base_increment * 2
        recommendation = f"Increase weight by {weight_increase} lbs"
    elif average_reps >= upper_range and high_rpe_count >= total_sets * 0.5:
        # Increase by base increment if at the upper range with high RPE
        weight_increase = base_increment
        recommendation = f"Increase weight by {weight_increase} lbs"
    elif average_reps >= lower_range:
        # Recommend maintaining current weight if within range but not at the top
        weight_increase = 0
        recommendation = "Maintain current weight"
    else:
        # Recommend a small increase or maintain if below range
        weight_increase = base_increment * 0.5
        recommendation = f"Maintain or increase weight by {weight_increase} lbs"

    # Calculate the recommended weight by adding the increase to the highest weight used
    recommended_weight = highest_weight + weight_increase

    # Update the exercise's recommended weight
    exercise.recWeight = recommended_weight
    exercise.save()

    return recommended_weight, recommendation
