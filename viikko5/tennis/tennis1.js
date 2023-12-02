'use strict';

function getScoreString(score) {
    if (score === 0) return 'Love'
    else if (score === 1) return 'Fifteen'
    else if (score === 2) return 'Thirty'
    else if (score === 3) return 'Forty'
    else return 'Unknown score'
}

function getScore(playerOneScore, playerTwoScore) {
    if (playerOneScore === playerTwoScore) {
        if (playerOneScore === 0) return 'Love-All';
        else if (playerOneScore === 1) return 'Fifteen-All';
        else if (playerOneScore === 2) return 'Thirty-All';
        else return 'Deuce'
    } else if (playerOneScore >= 4 || playerTwoScore >= 4) {
        const scoreDifference = Math.abs(playerOneScore - playerTwoScore);
        const winningPlayer = playerOneScore > playerTwoScore ? 'player1' : 'player2';

        if (scoreDifference === 1) return `Advantage ${winningPlayer}`;
        else return `Win for ${winningPlayer}`;
    } else {
        return `${getScoreString(playerOneScore)}-${getScoreString(playerTwoScore)}`
    }
}

module.exports = getScore;
