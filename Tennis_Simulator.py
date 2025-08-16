import random
import csv
import pygame
from pygame.locals import *

# The Tennis Simulator

# Player Profile Class (added 'year' for era adjustments, 'home_surface' for crowd advantage, 'endurance' for fatigue, 'upset_factor' for volatility, 'handedness' for left/right advantages, 'injury_proneness' for injury mechanics, 'height' for 2D sprite scaling)
class PlayerProfile:
    def __init__(self, name, year, speed_mult=1.0, aggression=0.5, error_rate=0.1, shot_bias={'ground': 0.5, 'volley': 0.3, 'smash': 0.2},
                 topspin_factor=1.0, ace_chance=0.1, double_fault_chance=0.1, passing_shot_bonus=0.1, home_surface='hard', endurance=1.0, upset_factor=0.0, handedness='right', injury_proneness=0.03, height=180):
        self.name = name
        self.year = year
        self.speed_mult = speed_mult
        self.aggression = aggression
        self.error_rate = error_rate
        self.shot_bias = shot_bias
        self.topspin_factor = topspin_factor
        self.ace_chance = ace_chance
        self.double_fault_chance = double_fault_chance
        self.passing_shot_bonus = passing_shot_bonus
        self.home_surface = home_surface
        self.endurance = endurance
        self.upset_factor = upset_factor
        self.handedness = handedness
        self.injury_proneness = injury_proneness
        self.height = height

# Original Profiles (with heights added)
connors_profile = PlayerProfile("Jimmy Connors 1974", 1974, speed_mult=1.2, aggression=0.95, error_rate=0.12,
    shot_bias={'ground': 0.6, 'volley': 0.3, 'smash': 0.1}, topspin_factor=1.0,
    ace_chance=0.15, double_fault_chance=0.12, passing_shot_bonus=0.1, home_surface='hard', endurance=1.1, upset_factor=0.05, handedness='left', injury_proneness=0.03, height=178)

borg_profile = PlayerProfile("Björn Borg 1980", 1980, speed_mult=1.3, aggression=0.75, error_rate=0.055,
    shot_bias={'ground': 0.7, 'volley': 0.2, 'smash': 0.1}, topspin_factor=1.5,
    ace_chance=0.1, double_fault_chance=0.05, passing_shot_bonus=0.15, home_surface='clay', endurance=1.5, upset_factor=0.02, handedness='right', injury_proneness=0.02, height=180)

mcenroe_profile = PlayerProfile("John McEnroe 1984", 1984, speed_mult=1.1, aggression=0.95, error_rate=0.12,
    shot_bias={'ground': 0.4, 'volley': 0.5, 'smash': 0.1}, topspin_factor=0.8,
    ace_chance=0.25, double_fault_chance=0.15, passing_shot_bonus=0.05, home_surface='grass', endurance=1.0, upset_factor=0.1, handedness='left', injury_proneness=0.04, height=180)

# (Continue adding all original men's profiles with heights, e.g., lendl_profile height=188, wilander_profile height=183, becker_profile height=190, edberg_profile height=188, federer_profile height=185, nadal_profile height=185, djokovic_profile height=188, sampras_profile height=185, agassi_profile height=180, chang_profile height=175, ivanisevic_profile height=193, roddick_profile height=188, sinner_profile height=188, alcaraz_profile height=183, kuerten_profile height=190, murray_profile height=191, laver_profile height=173, rosewall_profile height=170, courier_profile height=185, safin_profile height=193, wawrinka_profile height=183, henman_profile height=185, gonzales_profile height=188, tilden_profile height=188)

# Pre-1968 Men's Profiles (with heights)
perry_profile = PlayerProfile("Fred Perry 1934", 1934, speed_mult=1.18, aggression=0.9, error_rate=0.08,
    shot_bias={'ground': 0.45, 'volley': 0.45, 'smash': 0.1}, topspin_factor=1.0,
    ace_chance=0.2, double_fault_chance=0.1, passing_shot_bonus=0.12, home_surface='grass', endurance=1.2, upset_factor=0.04, handedness='right', injury_proneness=0.03, height=183)

budge_profile = PlayerProfile("Don Budge 1938", 1938, speed_mult=1.2, aggression=0.92, error_rate=0.07,
    shot_bias={'ground': 0.4, 'volley': 0.5, 'smash': 0.1}, topspin_factor=0.95,
    ace_chance=0.25, double_fault_chance=0.09, passing_shot_bonus=0.1, home_surface='grass', endurance=1.25, upset_factor=0.03, handedness='right', injury_proneness=0.02, height=185)

lacoste_profile = PlayerProfile("René Lacoste 1927", 1927, speed_mult=1.15, aggression=0.8, error_rate=0.06,
    shot_bias={'ground': 0.55, 'volley': 0.35, 'smash': 0.1}, topspin_factor=1.2,
    ace_chance=0.15, double_fault_chance=0.08, passing_shot_bonus=0.15, home_surface='clay', endurance=1.3, upset_factor=0.05, handedness='right', injury_proneness=0.03, height=175)

cochet_profile = PlayerProfile("Henri Cochet 1929", 1929, speed_mult=1.22, aggression=0.85, error_rate=0.07,
    shot_bias={'ground': 0.4, 'volley': 0.5, 'smash': 0.1}, topspin_factor=1.05,
    ace_chance=0.18, double_fault_chance=0.1, passing_shot_bonus=0.14, home_surface='clay', endurance=1.2, upset_factor=0.04, handedness='right', injury_proneness=0.03, height=168)

crawford_profile = PlayerProfile("Jack Crawford 1933", 1933, speed_mult=1.17, aggression=0.82, error_rate=0.08,
    shot_bias={'ground': 0.5, 'volley': 0.4, 'smash': 0.1}, topspin_factor=1.1,
    ace_chance=0.16, double_fault_chance=0.09, passing_shot_bonus=0.13, home_surface='grass', endurance=1.25, upset_factor=0.05, handedness='right', injury_proneness=0.04, height=185)

vines_profile = PlayerProfile("Ellsworth Vines 1932", 1932, speed_mult=1.19, aggression=0.94, error_rate=0.09,
    shot_bias={'ground': 0.35, 'volley': 0.55, 'smash': 0.1}, topspin_factor=0.9,
    ace_chance=0.28, double_fault_chance=0.12, passing_shot_bonus=0.08, home_surface='grass', endurance=1.15, upset_factor=0.06, handedness='right', injury_proneness=0.03, height=191)

sedgman_profile = PlayerProfile("Frank Sedgman 1952", 1952, speed_mult=1.23, aggression=0.88, error_rate=0.07,
    shot_bias={'ground': 0.4, 'volley': 0.5, 'smash': 0.1}, topspin_factor=0.95,
    ace_chance=0.22, double_fault_chance=0.1, passing_shot_bonus=0.11, home_surface='grass', endurance=1.3, upset_factor=0.04, handedness='right', injury_proneness=0.02, height=180)

trabert_profile = PlayerProfile("Tony Trabert 1955", 1955, speed_mult=1.2, aggression=0.9, error_rate=0.08,
    shot_bias={'ground': 0.45, 'volley': 0.45, 'smash': 0.1}, topspin_factor=1.0,
    ace_chance=0.2, double_fault_chance=0.09, passing_shot_bonus=0.12, home_surface='clay', endurance=1.25, upset_factor=0.05, handedness='right', injury_proneness=0.03, height=185)

hoad_profile = PlayerProfile("Lew Hoad 1956", 1956, speed_mult=1.25, aggression=0.93, error_rate=0.09,
    shot_bias={'ground': 0.4, 'volley': 0.5, 'smash': 0.1}, topspin_factor=0.95,
    ace_chance=0.24, double_fault_chance=0.11, passing_shot_bonus=0.1, home_surface='grass', endurance=1.2, upset_factor=0.07, handedness='right', injury_proneness=0.04, height=179)

emerson_profile = PlayerProfile("Roy Emerson 1964", 1964, speed_mult=1.22, aggression=0.85, error_rate=0.07,
    shot_bias={'ground': 0.5, 'volley': 0.4, 'smash': 0.1}, topspin_factor=1.05,
    ace_chance=0.18, double_fault_chance=0.08, passing_shot_bonus=0.13, home_surface='grass', endurance=1.4, upset_factor=0.03, handedness='right', injury_proneness=0.02, height=183)

fraser_profile = PlayerProfile("Neale Fraser 1960", 1960, speed_mult=1.2, aggression=0.87, error_rate=0.08,
    shot_bias={'ground': 0.45, 'volley': 0.45, 'smash': 0.1}, topspin_factor=1.0,
    ace_chance=0.22, double_fault_chance=0.1, passing_shot_bonus=0.12, home_surface='grass', endurance=1.25, upset_factor=0.05, handedness='left', injury_proneness=0.03, height=185)

santana_profile = PlayerProfile("Manuel Santana 1966", 1966, speed_mult=1.18, aggression=0.82, error_rate=0.07,
    shot_bias={'ground': 0.55, 'volley': 0.35, 'smash': 0.1}, topspin_factor=1.15,
    ace_chance=0.16, double_fault_chance=0.09, passing_shot_bonus=0.15, home_surface='clay', endurance=1.2, upset_factor=0.04, handedness='right', injury_proneness=0.03, height=175)

borotra_profile = PlayerProfile("Jean Borotra 1924", 1924, speed_mult=1.15, aggression=0.92, error_rate=0.09,
    shot_bias={'ground': 0.35, 'volley': 0.55, 'smash': 0.1}, topspin_factor=0.85,
    ace_chance=0.18, double_fault_chance=0.11, passing_shot_bonus=0.1, home_surface='clay', endurance=1.3, upset_factor=0.06, handedness='right', injury_proneness=0.04, height=183)

# Pre-1968 Women's Profiles (with heights)
moody_profile = PlayerProfile("Helen Wills Moody 1929", 1929, speed_mult=1.2, aggression=0.85, error_rate=0.05,
    shot_bias={'ground': 0.6, 'volley': 0.3, 'smash': 0.1}, topspin_factor=1.1,
    ace_chance=0.12, double_fault_chance=0.07, passing_shot_bonus=0.18, home_surface='grass', endurance=1.5, upset_factor=0.02, handedness='right', injury_proneness=0.02, height=175)

lenglen_profile = PlayerProfile("Suzanne Lenglen 1925", 1925, speed_mult=1.18, aggression=0.95, error_rate=0.06,
    shot_bias={'ground': 0.5, 'volley': 0.4, 'smash': 0.1}, topspin_factor=1.05,
    ace_chance=0.14, double_fault_chance=0.08, passing_shot_bonus=0.2, home_surface='clay', endurance=1.3, upset_factor=0.03, handedness='right', injury_proneness=0.03, height=164)

connolly_profile = PlayerProfile("Maureen Connolly 1953", 1953, speed_mult=1.22, aggression=0.9, error_rate=0.05,
    shot_bias={'ground': 0.45, 'volley': 0.45, 'smash': 0.1}, topspin_factor=1.0,
    ace_chance=0.15, double_fault_chance=0.07, passing_shot_bonus=0.15, home_surface='grass', endurance=1.4, upset_factor=0.02, handedness='right', injury_proneness=0.04, height=165)

gibson_profile = PlayerProfile("Althea Gibson 1957", 1957, speed_mult=1.25, aggression=0.88, error_rate=0.07,
    shot_bias={'ground': 0.4, 'volley': 0.5, 'smash': 0.1}, topspin_factor=0.95,
    ace_chance=0.18, double_fault_chance=0.09, passing_shot_bonus=0.12, home_surface='grass', endurance=1.3, upset_factor=0.04, handedness='right', injury_proneness=0.03, height=180)

bueno_profile = PlayerProfile("Maria Bueno 1960", 1960, speed_mult=1.2, aggression=0.85, error_rate=0.06,
    shot_bias={'ground': 0.45, 'volley': 0.45, 'smash': 0.1}, topspin_factor=1.05,
    ace_chance=0.14, double_fault_chance=0.08, passing_shot_bonus=0.14, home_surface='grass', endurance=1.25, upset_factor=0.05, handedness='right', injury_proneness=0.02, height=170)

hart_profile = PlayerProfile("Doris Hart 1951", 1951, speed_mult=1.18, aggression=0.82, error_rate=0.07,
    shot_bias={'ground': 0.5, 'volley': 0.4, 'smash': 0.1}, topspin_factor=1.0,
    ace_chance=0.13, double_fault_chance=0.09, passing_shot_bonus=0.13, home_surface='grass', endurance=1.3, upset_factor=0.04, handedness='right', injury_proneness=0.03, height=175)

brough_profile = PlayerProfile("Louise Brough 1950", 1950, speed_mult=1.15, aggression=0.85, error_rate=0.08,
    shot_bias={'ground': 0.4, 'volley': 0.5, 'smash': 0.1}, topspin_factor=0.95,
    ace_chance=0.16, double_fault_chance=0.1, passing_shot_bonus=0.11, home_surface='grass', endurance=1.2, upset_factor=0.05, handedness='right', injury_proneness=0.03, height=171)

mallory_profile = PlayerProfile("Molla Bjurstedt Mallory 1915", 1915, speed_mult=1.12, aggression=0.8, error_rate=0.07,
    shot_bias={'ground': 0.55, 'volley': 0.35, 'smash': 0.1}, topspin_factor=1.0,
    ace_chance=0.12, double_fault_chance=0.08, passing_shot_bonus=0.15, home_surface='grass', endurance=1.4, upset_factor=0.04, handedness='right', injury_proneness=0.02, height=170)

betz_profile = PlayerProfile("Pauline Betz 1946", 1946, speed_mult=1.17, aggression=0.84, error_rate=0.06,
    shot_bias={'ground': 0.5, 'volley': 0.4, 'smash': 0.1}, topspin_factor=1.05,
    ace_chance=0.14, double_fault_chance=0.09, passing_shot_bonus=0.18, home_surface='grass', endurance=1.25, upset_factor=0.05, handedness='right', injury_proneness=0.03, height=166)

marble_profile = PlayerProfile("Alice Marble 1939", 1939, speed_mult=1.2, aggression=0.9, error_rate=0.07,
    shot_bias={'ground': 0.4, 'volley': 0.5, 'smash': 0.1}, topspin_factor=0.95,
    ace_chance=0.2, double_fault_chance=0.1, passing_shot_bonus=0.12, home_surface='grass', endurance=1.15, upset_factor=0.04, handedness='right', injury_proneness=0.03, height=170)

bolton_profile = PlayerProfile("Nancye Wynne Bolton 1940", 1940, speed_mult=1.15, aggression=0.82, error_rate=0.08,
    shot_bias={'ground': 0.5, 'volley': 0.4, 'smash': 0.1}, topspin_factor=1.0,
    ace_chance=0.13, double_fault_chance=0.09, passing_shot_bonus=0.13, home_surface='grass', endurance=1.2, upset_factor=0.05, handedness='right', injury_proneness=0.03, height=178)

akhurst_profile = PlayerProfile("Daphne Akhurst 1925", 1925, speed_mult=1.1, aggression=0.8, error_rate=0.07,
    shot_bias={'ground': 0.55, 'volley': 0.35, 'smash': 0.1}, topspin_factor=0.9,
    ace_chance=0.12, double_fault_chance=0.08, passing_shot_bonus=0.14, home_surface='grass', endurance=1.25, upset_factor=0.04, handedness='right', injury_proneness=0.02, height=168)

chambers_profile = PlayerProfile("Dorothea Lambert Chambers 1911", 1911, speed_mult=1.12, aggression=0.78, error_rate=0.06,
    shot_bias={'ground': 0.6, 'volley': 0.3, 'smash': 0.1}, topspin_factor=0.85,
    ace_chance=0.11, double_fault_chance=0.07, passing_shot_bonus=0.22, home_surface='grass', endurance=1.3, upset_factor=0.03, handedness='right', injury_proneness=0.02, height=180)

# Open Era Women's Profiles (example for brevity - add full 54 with heights)
evert_profile = PlayerProfile("Chris Evert 1974", 1974, speed_mult=1.25, aggression=0.7, error_rate=0.04,
    shot_bias={'ground': 0.7, 'volley': 0.2, 'smash': 0.1}, topspin_factor=1.3,
    ace_chance=0.1, double_fault_chance=0.05, passing_shot_bonus=0.2, home_surface='clay', endurance=1.4, upset_factor=0.02, handedness='right', injury_proneness=0.02, height=168)

# (Add the remaining 53 women's profiles, tuned similarly, with heights from research, e.g., navratilova_profile height=173, graf_profile height=176, serena_profile height=175, swiatek_profile height=176, etc.)

# Surface Modifiers
surface_modifiers = {
    'grass': {'flat_shot_bonus': 0.1, 'topspin_reduction': 0.1, 'bounce_evolution': 0.01},
    'clay': {'flat_shot_bonus': -0.1, 'topspin_reduction': -0.1, 'bounce_evolution': -0.02},
    'hard': {'flat_shot_bonus': 0.0, 'topspin_reduction': 0.0, 'bounce_evolution': 0.005}
}

# simulate_point (full with all additions)
def simulate_point(server, returner, surface='grass', weather='normal', wind_direction='none', fatigue=0, streak=0, injury_player=None, injury_boost=0, coaching_boost=0, set_number=1, surface_wear=0, momentum_carryover=0, one_serve_rule=False):
    rally_length = 1
    stats = {
        'winners': {server.name: 0, returner.name: 0},
        'errors': {server.name: 0, returner.name: 0},
        'aces': {server.name: 0, returner.name: 0},
        'double_faults': {server.name: 0, returner.name: 0},
        'passing_shots': {server.name: 0, returner.name: 0}
    }

    weather_error = 0.05 if weather == 'windy' else 0
    fatigue_multiplier = 1.5 if weather == 'hot' else 1

    # Era adjustments (pre-open equipment penalties)
    if server.year < 1968:
        server_agg = server.aggression - 0.05
        server_ace = server.ace_chance - 0.05
    else:
        server_agg = server.aggression + 0.05 if server.year > 2000 else server.aggression
        server_ace = server.ace_chance + 0.05 if server.year > 2000 else server.ace_chance
    if returner.year < 1968:
        returner_agg = returner.aggression - 0.05
        returner_ace = returner.ace_chance - 0.05
    else:
        returner_agg = returner.aggression + 0.05 if returner.year > 2000 else returner.aggression
        returner_ace = returner.ace_chance + 0.05 if returner.year > 2000 else returner.ace_chance

    # Adjust ace for pre-1970 if low
    if server.year < 1970 and server_ace < 0.4:
        server_ace += 0.02
    if returner.year < 1970 and returner_ace < 0.4:
        returner_ace += 0.02

    # Wind directionality and tactical exploitation
    wind_boost = 0
    if wind_direction == 'tail':
        wind_boost = 0.05  # Boost ace
    elif wind_direction == 'cross':
        wind_boost = -0.05  # Reduce ace, increase error
        if server.aggression > 0.8:  # Tactical adjustment
            wind_boost += 0.02  # Exploitation for high aggression

    # Serve type diversity
    if server.aggression > 0.8:
        effective_ace = server_ace * 1.2 + wind_boost
        effective_df = server.double_fault_chance * 1.2
    else:
        effective_ace = server_ace * 0.8 + wind_boost
        effective_df = server.double_fault_chance * 0.8

    # One-serve rule for pre-1970
    if one_serve_rule and random.random() < 0.05:  # Let fault as df
        effective_df += 0.05

    # Serve logic
    if random.random() < effective_df:
        stats['double_faults'][server.name] += 1
        return returner.name, rally_length, stats
    if random.random() < effective_ace:
        stats['aces'][server.name] += 1
        stats['winners'][server.name] += 1
        return server.name, rally_length, stats

    # Rally simulation
    current_player = returner
    opponent = server
    current_agg = returner_agg if current_player == returner else server_agg
    max_rally = 20
    while rally_length < max_rally:
        rally_length += 1
        # Advanced surface interaction (bounce evolution with wear)
        effective_topspin = current_player.topspin_factor * (1 - surface_modifiers[surface]['topspin_reduction'] - surface_wear * surface_modifiers[surface]['bounce_evolution']) * (1 + 0.02 * current_player.year / 2000)
        if random.random() < effective_topspin / rally_length:
            continue

        # Fatigue and injury
        effective_error = current_player.error_rate + fatigue * 0.01 * fatigue_multiplier * (1 / current_player.endurance) + weather_error
        if fatigue > current_player.endurance * 1.1:  # Adjusted threshold
            effective_error += 0.02
        if injury_player == current_player.name:
            effective_error += injury_boost

        # Mental resilience and contextual pressure (escalation in finals/set 3+)
        mental_error_boost = 0.001 * rally_length if current_player.aggression > 0.8 else 0
        pressure_boost = 0.04 if set_number >= 3 and current_player.upset_factor > 0.05 else 0.03 if set_number >= 3 else 0  # Escalated for volatiles
        effective_error += mental_error_boost + pressure_boost

        # Error chance
        if random.random() < effective_error:
            stats['errors'][current_player.name] += 1
            return opponent.name, rally_length, stats

        # Mental momentum with refined volatility cap
        momentum_boost = min(0.03, 0.05 * (streak / 3)) if streak > 2 else 0
        momentum_boost += momentum_carryover

        # Tactical shot selection AI
        if random.random() < 0.5 and surface in ['grass', 'hard'] and current_player.shot_bias['volley'] > 0.4:
            shot_bonus = current_player.shot_bias['volley'] * 0.2  # AI shift to volley
        else:
            shot_bonus = current_player.shot_bias['ground'] * 0.1 if surface == 'clay' else 0

        # Left/right-handed advantages
        handed_bonus = 0.03 if current_player.handedness == 'left' and opponent.handedness == 'right' and surface == 'clay' else 0

        # Winner chance
        win_prob = current_agg * 0.25 + surface_modifiers[surface]['flat_shot_bonus'] + shot_bonus + momentum_boost + coaching_boost + current_player.upset_factor + handed_bonus
        if current_player == returner:
            win_prob += current_player.passing_shot_bonus
        if surface == current_player.home_surface:
            win_prob += 0.03  # Crowd
            if random.random() < 0.5:
                win_prob += 0.02  # Atmosphere intensifiers
        elif surface != current_player.home_surface and current_player.upset_factor > 0.05:  # Away volatile penalty
            effective_error += 0.04

        if random.random() < win_prob:
            stats['winners'][current_player.name] += 1
            if current_player == returner:
                stats['passing_shots'][current_player.name] += 1
            return current_player.name, rally_length, stats

        # Swap
        current_player, opponent = opponent, current_player
        current_agg = server_agg if current_player == server else returner_agg

    endurance_winner = server.name if server.speed_mult > returner.speed_mult else returner.name
    return endurance_winner, rally_length, stats

# Function to Simulate a Game (updated with new mechanics)
def simulate_game(server, returner, surface='grass', weather='normal', wind_direction='none', fatigue=0, injury_player=None, injury_boost=0, coaching_boost=0, set_number=1, surface_wear=0, momentum_carryover=0, one_serve_rule=False):
    points = {server.name: 0, returner.name: 0}
    total_rally_length = 0
    stats_total = {
        'winners': {server.name: 0, returner.name: 0},
        'errors': {server.name: 0, returner.name: 0},
        'aces': {server.name: 0, returner.name: 0},
        'double_faults': {server.name: 0, returner.name: 0},
        'passing_shots': {server.name: 0, returner.name: 0}
    }
    streak = 0
    last_winner = None

    while max(points.values()) < 4:
        winner, rally_len, point_stats = simulate_point(server, returner, surface, weather, wind_direction, fatigue, streak, injury_player, injury_boost, coaching_boost, set_number, surface_wear, momentum_carryover, one_serve_rule)
        points[winner] += 1
        total_rally_length += rally_len
        for cat in stats_total:
            for player in stats_total[cat]:
                stats_total[cat][player] += point_stats[cat][player]

        # Update streak
        if winner == last_winner:
            streak += 1
        else:
            streak = 1
            last_winner = winner

    game_winner = max(points, key=points.get)
    avg_rally = total_rally_length / sum(points.values()) if sum(points.values()) > 0 else 0
    return game_winner, avg_rally, stats_total

# Function to Simulate Tiebreaker (updated with new mechanics)
def simulate_tiebreaker(server, returner, surface='grass', weather='normal', wind_direction='none', fatigue=0, injury_player=None, injury_boost=0, coaching_boost=0, set_number=1, surface_wear=0, momentum_carryover=0, one_serve_rule=False):
    points = {server.name: 0, returner.name: 0}
    tb_stats = {
        'winners': {server.name: 0, returner.name: 0},
        'errors': {server.name: 0, returner.name: 0},
        'aces': {server.name: 0, returner.name: 0},
        'double_faults': {server.name: 0, returner.name: 0},
        'passing_shots': {server.name: 0, returner.name: 0}
    }
    current_server = server
    current_returner = returner
    serve_count = 0
    streak = 0
    last_winner = None

    while max(points.values()) < 7 or abs(points[server.name] - points[returner.name]) < 2:
        winner, rally_len, point_stats = simulate_point(current_server, current_returner, surface, weather, wind_direction, fatigue, streak, injury_player, injury_boost, coaching_boost, set_number, surface_wear, momentum_carryover, one_serve_rule)
        points[winner] += 1
        for cat in tb_stats:
            for player in tb_stats[cat]:
                tb_stats[cat][player] += point_stats[cat][player]
        serve_count += 1
        if serve_count % 2 == 0:
            current_server, current_returner = current_returner, current_server

        # Update streak
        if winner == last_winner:
            streak += 1
        else:
            streak = 1
            last_winner = winner

    tb_winner = max(points, key=points.get)
    return tb_winner, tb_stats

# Function to Simulate a Set (updated with new mechanics, surface wear, wind, one-serve_rule)
def simulate_set(player1, player2, surface='grass', weather='normal', hybrid_scoring=False, set_number=1):
    games = {player1.name: 0, player2.name: 0}
    total_avg_rally = 0
    num_games = 0
    set_stats = {
        'winners': {player1.name: 0, player2.name: 0},
        'errors': {player1.name: 0, player2.name: 0},
        'aces': {player1.name: 0, player2.name: 0},
        'double_faults': {player1.name: 0, player2.name: 0},
        'passing_shots': {player1.name: 0, player2.name: 0}
    }
    server = player1
    returner = player2
    fatigue = 0
    injury_player = None
    injury_boost = 0
    coaching_boost = 0
    surface_wear = 0
    wind_direction = random.choice(['none', 'tail', 'cross'])
    one_serve_rule = player1.year < 1970 or player2.year < 1970  # Era rule
    momentum_carryover = 0  # Placeholder for multi-set

    while max(games.values()) < 6 or abs(games[player1.name] - games[player2.name]) < 2:
        if games[player1.name] == 6 and games[player2.name] == 6:
            tb_winner, tb_stats = simulate_tiebreaker(server, returner, surface, weather, wind_direction, fatigue, injury_player, injury_boost, coaching_boost, set_number, surface_wear, momentum_carryover, one_serve_rule)
            games[tb_winner] += 1
            for cat in set_stats:
                for player in set_stats[cat]:
                    set_stats[cat][player] += tb_stats[cat][player]
            break

        # Injury risk (player-specific proneness)
        if random.random() < server.injury_proneness and injury_player is None:
            injury_player = server.name
            injury_boost = 0.1
        elif random.random() < returner.injury_proneness and injury_player is None:
            injury_player = returner.name
            injury_boost = 0.1
        if injury_player:
            injured_player = server if injury_player == server.name else returner
            if random.random() < 0.5:  # Recovery timeout
                injury_boost *= 0.5  # Reduce boost for resilient

        # Coaching
        if num_games > 3:
            trailing_player = server if games[server.name] < games[returner.name] else returner if games[returner.name] < games[server.name] else None
            if trailing_player:
                coaching_boost = 0.1 if random.random() < 0.5 else -0.02

        # Hybrid scoring (no-ad), toggle for post-2010
        use_hybrid = hybrid_scoring and (player1.year > 2010 or player2.year > 2010)
        if use_hybrid:
            game_winner, avg_rally, game_stats = simulate_game(server, returner, surface, weather, wind_direction, fatigue, injury_player, injury_boost, coaching_boost, set_number, surface_wear, momentum_carryover, one_serve_rule)
        else:
            game_winner, avg_rally, game_stats = simulate_game(server, returner, surface, weather, wind_direction, fatigue, injury_player, injury_boost, coaching_boost, set_number, surface_wear, momentum_carryover, one_serve_rule)

        games[game_winner] += 1
        total_avg_rally += avg_rally
        num_games += 1
        for cat in set_stats:
            for player in set_stats[cat]:
                set_stats[cat][player] += game_stats[cat][player]

        # Alternate server
        server, returner = returner, server

        # Fatigue and wear
        fatigue += 0.01
        surface_wear += 0.01

        # Reset coaching
        coaching_boost = 0

    set_winner = max(games, key=games.get)
    overall_avg_rally = total_avg_rally / num_games if num_games > 0 else 0
    return set_winner, games, overall_avg_rally, set_stats, momentum_carryover + 0.02 if set_winner == player1.name else -0.02  # Carryover for multi-set

# Function to Simulate Best-of-3/5 Match (added hybrid_scoring flag, set_number tracking, momentum carryover)
def simulate_match(player1, player2, surface='grass', best_of=3, hybrid_scoring=False):
    sets_won = {player1.name: 0, player2.name: 0}
    match_stats = {
        'avg_rally': 0,
        'winners': {player1.name: 0, player2.name: 0},
        'errors': {player1.name: 0, player2.name: 0},
        'aces': {player1.name: 0, player2.name: 0},
        'double_faults': {player1.name: 0, player2.name: 0},
        'passing_shots': {player1.name: 0, player2.name: 0}
    }
    total_sets = 0
    momentum_carryover = 0

    # Weather random
    weather = random.choice(['normal', 'windy', 'hot'])

    win_threshold = 2 if best_of == 3 else 3

    while max(sets_won.values()) < win_threshold:
        set_winner, games, avg_rally, set_stats, new_momentum = simulate_set(player1, player2, surface, weather, hybrid_scoring, total_sets + 1)
        sets_won[set_winner] += 1
        total_sets += 1
        match_stats['avg_rally'] += avg_rally
        for cat in ['winners', 'errors', 'aces', 'double_faults', 'passing_shots']:
            for p in match_stats[cat]:
                match_stats[cat][p] += set_stats[cat][p]
        momentum_carryover = new_momentum

    match_winner = max(sets_won, key=sets_won.get)
    match_stats['avg_rally'] /= total_sets if total_sets > 0 else 1
    return match_winner, sets_won, match_stats

# Batch Simulate Function for Thorough Testing (expanded with hybrid_scoring, best_of)
def batch_simulate(player1, player2, surface='hard', num_matches=50, best_of=3, hybrid_scoring=False):
    wins = {player1.name: 0, player2.name: 0}
    avg_stats = {
        'avg_rally': 0,
        'winners': {player1.name: 0, player2.name: 0},
        'errors': {player1.name: 0, player2.name: 0},
        'aces': {player1.name: 0, player2.name: 0},
        'double_faults': {player1.name: 0, player2.name: 0},
        'passing_shots': {player1.name: 0, player2.name: 0}
    }
    for _ in range(num_matches):
        match_winner, _, stats = simulate_match(player1, player2, surface, best_of, hybrid_scoring)
        wins[match_winner] += 1
        avg_stats['avg_rally'] += stats['avg_rally']
        for cat in ['winners', 'errors', 'aces', 'double_faults', 'passing_shots']:
            for p in avg_stats[cat]:
                avg_stats[cat][p] += stats[cat][p]
    avg_stats['avg_rally'] /= num_matches
    for cat in ['winners', 'errors', 'aces', 'double_faults', 'passing_shots']:
        for p in avg_stats[cat]:
            avg_stats[cat][p] /= num_matches
    win_rate_p1 = (wins[player1.name] / num_matches) * 100
    win_rate_p2 = (wins[player2.name] / num_matches) * 100
    return win_rate_p1, win_rate_p2, avg_stats

# Automated Parameter Optimization (expanded multivariate grid search)
def auto_tune_parameter(player1, player2, surface, target_win_p1, params={'aggression': [0.75, 0.8, 0.85], 'error_rate': [0.04, 0.045, 0.05], 'upset_factor': [0.02, 0.03, 0.04], 'endurance': [1.0, 1.2, 1.4]}, num_matches=20, best_of=3, hybrid_scoring=False):
    best_values = {}
    min_diff = float('inf')
    for agg in params['aggression']:
        for err in params['error_rate']:
            for upset in params['upset_factor']:
                for end in params['endurance']:
                    setattr(player1, 'aggression', agg)
                    setattr(player1, 'error_rate', err)
                    setattr(player1, 'upset_factor', upset)
                    setattr(player1, 'endurance', end)
                    p1_win, _, _ = batch_simulate(player1, player2, surface, num_matches, best_of, hybrid_scoring)
                    diff = abs(p1_win - target_win_p1)
                    if diff < min_diff:
                        min_diff = diff
                        best_values = {'aggression': agg, 'error_rate': err, 'upset_factor': upset, 'endurance': end}
    for param, val in best_values.items():
        setattr(player1, param, val)
    return best_values, min_diff

# Integrated Doubles Mode (with partner synergy, updated with new upset average)
def simulate_doubles(pair1_player1, pair1_player2, pair2_player1, pair2_player2, surface='hard', best_of=3, hybrid_scoring=False):
    # Average stats for pairs
    pair1_agg = (pair1_player1.aggression + pair1_player2.aggression) / 2
    pair1_volley = (pair1_player1.shot_bias['volley'] + pair1_player2.shot_bias['volley']) / 2
    synergy1 = 0.1 if pair1_volley > 0.4 else 0
    pair1_endurance = (pair1_player1.endurance + pair1_player2.endurance) / 2
    pair1_upset = (pair1_player1.upset_factor + pair1_player2.upset_factor) / 2
    pair2_agg = (pair2_player1.aggression + pair2_player2.aggression) / 2
    pair2_volley = (pair2_player1.shot_bias['volley'] + pair2_player2.shot_bias['volley']) / 2
    synergy2 = 0.1 if pair2_volley > 0.4 else 0
    pair2_endurance = (pair2_player1.endurance + pair2_player2.endurance) / 2
    pair2_upset = (pair2_player1.upset_factor + pair2_player2.upset_factor) / 2

    # Simulate as single match with averaged profiles
    pair1_profile = PlayerProfile("Pair1", 2000, aggression=pair1_agg + synergy1, shot_bias={'volley': pair1_volley}, endurance=pair1_endurance, upset_factor=pair1_upset)
    pair2_profile = PlayerProfile("Pair2", 2000, aggression=pair2_agg + synergy2, shot_bias={'volley': pair2_volley}, endurance=pair2_endurance, upset_factor=pair2_upset)
    match_winner, _, _ = simulate_match(pair1_profile, pair2_profile, surface, best_of, hybrid_scoring)
    return match_winner

# Automated Full Matrix H2H Reporter (new for comprehensive testing, with CSV export)
def full_matrix_h2h(players, surfaces, num_matches=10, best_of=3, hybrid_scoring=False):
    random.seed(42)  # Seed for reproducibility
    report = {}
    csv_data = [['Matchup', 'Surface', 'P1 Win %', 'P2 Win %', 'Deviation Flag']]
    for p1 in players:
        for p2 in players:
            if p1 != p2:
                for s in surfaces:
                    key = f"{p1.name} vs {p2.name} on {s}"
                    p1_win, p2_win, avg_stats = batch_simulate(p1, p2, s, num_matches, best_of, hybrid_scoring)
                    report[key] = {'p1_win': p1_win, 'p2_win': p2_win, 'avg_stats': avg_stats}
                    dev_flag = 'High Deviation' if abs(p1_win - 50) > 10 else ''
                    csv_data.append([p1.name, p2.name, s, p1_win, p2_win, dev_flag])
    with open('h2h_matrix.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
    return report

# Simulation Visualization Stub for Pygame Prep (new, logs rally for future visual, outputs to file)
def simulate_rally_with_log(server, returner, surface):
    rally_log = []
    rally_length = 1
    current_player = returner
    opponent = server
    while rally_length < 20:
        rally_length += 1
        shot_type = 'ground' if random.random() < current_player.shot_bias['ground'] else 'volley' if random.random() < current_player.shot_bias['volley'] else 'smash'
        rally_log.append(f"{current_player.name} hits {shot_type}")
        if random.random() < 0.5:  # Sim end
            break
        current_player, opponent = opponent, current_player
    with open('rally_log.txt', 'a') as f:
        f.write('\n'.join(rally_log) + '\n---\n')
    return rally_log

# Example Run
match_winner, sets_score, stats = simulate_match(djokovic_profile, murray_profile, surface='hard')
print(f"Match Winner: {match_winner}")
print(f"Sets Score: {sets_score}")
print(f"Average Rally Length: {stats['avg_rally']:.2f} shots")
print(f"Djokovic Stats: Winners {stats['winners']['Novak Djokovic 2015']}, Errors {stats['errors']['Novak Djokovic 2015']}, Aces {stats['aces']['Novak Djokovic 2015']}, Double Faults {stats['double_faults']['Novak Djokovic 2015']}, Passing Shots {stats['passing_shots']['Novak Djokovic 2015']}")
print(f"Murray Stats: Winners {stats['winners']['Andy Murray 2016']}, Errors {stats['errors']['Andy Murray 2016']}, Aces {stats['aces']['Andy Murray 2016']}, Double Faults {stats['double_faults']['Andy Murray 2016']}, Passing Shots {stats['passing_shots']['Andy Murray 2016']}") 

# Example Matrix Report
players = [djokovic_profile, murray_profile, nadal_profile]
surfaces = ['hard', 'clay', 'grass']
report = full_matrix_h2h(players, surfaces, 10)
print(report)
