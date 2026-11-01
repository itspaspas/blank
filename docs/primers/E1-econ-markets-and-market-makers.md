# E1 — Markets and market makers: the economics from zero

*Primer for the project "Market Making under Cross-Asset Hawkes Order Flow". Written 2026-10-26
for a reader who is new to both the economics and the mathematics.*

---

## How to read this

This file explains the **economic world** the project's mathematics describes: what a market is,
what a market maker does, why they quote the way they do, and what "optimal quotes" means for a
trading desk. It needs no mathematics beyond arithmetic. A few formulas appear, and each one is
explained term by term with numbers.

Each section has the same shape:

1. **Intuition**: plain words and a small picture.
2. **Worked example**: actual numbers you can redo with a calculator.
3. **Formal statement**: the version that appears in the papers, in the project's notation
   (CLAUDE.md, "Notation and equations").
4. **Why it matters here**: the link to the research design and plan.
5. **In one breath**: a 3–5 line recap.

Self-check questions with short answers are collected at the end of the file.

**Sibling primers** (all in `docs/primers/`):
- `M1-math-foundations.md`: probability, Poisson and Hawkes processes, Itô calculus, linear algebra.
- `M2-math-control-and-models.md`: optimal control, the HJB equation, and the models
  Avellaneda–Stoikov, GLFT 2013, BEGV 2021, CJR 2014, Barzykin 2026b.
- `M3-math-this-project.md`: the project's own mathematics (lifted HJB, perturbation, numerics,
  regret).
- `E2-econ-order-flow-and-this-project.md`: order flow as a process, clustering, the research
  story, the key papers in plain language, and a **full glossary**.

When this file needs a mathematical object (a Poisson process, the HJB equation), it explains only
what you need for the economics and sends you to the M-files for the rest.

**Citation conventions.** Claims about a specific paper cite the wiki page as
(Author Year, wiki: [[slug]]) with page or equation numbers where the wiki gives them. Statements
not attributed to a paper are general textbook knowledge. Arithmetic marked "(my arithmetic)" was
done for this primer from a formula in a cited source. Project claims that are derived but not yet
verified carry the tag **[D]**, as in the design and synthesis pages.

---

## Table of contents

1. What a market is
2. What is traded: stocks, bonds, FX, futures, options
3. Where it is traded: exchanges, OTC dealer markets, RFQ
4. The limit order book: bid, ask, mid, spread, tick, depth, orders, aggressor
5. Market makers: who they are and how they earn
6. Inventory, inventory risk and quote skew
7. Several assets: correlation, hedging and cross-hedging
8. Adverse selection and informed flow
9. Liquidity
10. Risk aversion in economic terms
11. PnL and mark-to-market accounting
12. What "optimal quotes" mean economically
13. What a model buys a trading desk
14. Regulation, very lightly
15. Map from economic words to project symbols
16. Self-check questions and answers

---

## 1. What a market is

### Intuition

A market is a place, physical or electronic, where people who want to buy something meet people
who want to sell it, and a price forms at which they agree to trade. The difficulty is **timing**.
A pension fund that wants to sell 10,000 shares at 10:03 rarely finds someone who wants to buy
exactly 10,000 shares at exactly 10:03. Buyers and sellers arrive at random moments, in random
sizes.

Picture a used-car market with no dealers. You want to sell your car today. Maybe a buyer comes
by this afternoon, maybe next week. If you need the money today, you will accept a low price.
Now add a **dealer** who is always there, buys your car immediately at a price somewhat below what
he hopes to resell it for, and sells it later to whoever arrives. The dealer sells **immediacy**:
the ability to trade *now* instead of waiting for the other side to show up. The gap between his
buying price and his selling price is what you pay for that service.

A **market maker** is exactly this dealer, in financial markets, operating at very high speed and
in very many small trades.

### The two basic economic functions of a market

- **Price discovery**: the market aggregates many people's information and opinions into one
  number, the price.
- **Liquidity provision**: the market lets you convert an asset into cash (or back) quickly, at a
  price close to its fair value, without moving the price much. Section 9 makes "liquidity" precise.

Market makers matter mostly for the second function. The models in this project treat the
"fair value" of the asset as given from outside (an exogenous random process, the mid-price
$S_t$), and ask only how the market maker should provide liquidity around it.

### Why it matters here

Everything in the project is about *how* a liquidity provider should set prices when buyers and
sellers arrive at random times, and specifically when those arrivals **cluster**: a burst of
activity tends to be followed by more activity (the subject of `E2-...` and of Hawkes processes in
`M1-...`).

### In one breath

A market lets buyers and sellers who arrive at different times trade. A market maker stands
in between, always ready to buy or sell, and charges a small price gap for that immediacy. The
project studies how that gap, and its position around fair value, should be set when arrivals
are random and clustered.

---

## 2. What is traded: stocks, bonds, FX, futures, options

An **asset** (also "instrument", "security", "contract") is anything with a price that can be
traded. The project's models are written for "$d$ assets" in general, so you need only a rough
picture of each class, and of which class each source paper uses.

### Stocks (equities)

A share is a small piece of ownership of a company. Shares of large companies trade on
**exchanges** (Section 3) through a **limit order book** (Section 4). Prices are quoted in currency
per share; the minimum price step (the **tick**) is typically one cent for US stocks priced above
one dollar.

*In the wiki:* GLFT 2013 illustrate their model on one day of France Telecom shares (15 March
2012) (Guéant et al. 2013, wiki: [[gueant-2013-dealing-inventory-risk]], §7, pp. 493–495). CJR
2014 fit their Hawkes model to IBM (Cartea et al. 2014, wiki: [[cartea-2014-buy-low-sell]],
App. A, pp. 435–436).

### Bonds

A bond is a loan in tradable form: the issuer (a government or company) promises fixed payments.
Corporate bonds trade mostly **over the counter** (OTC) through dealers, often by **request for
quote** (RFQ, Section 3). Many bonds trade rarely, so liquidity is thin and dealers carry
inventory for a long time.

*In the wiki:* the two-asset numerical example of BEGV 2021 uses RFQ-style parameters (30 requests
per day, prices around 100 €) (Bergault et al. 2021, wiki: [[bergault-2021-closed-form-approximations]],
Sec. 6, pp. 130–131); Bergault & Guéant 2023 work on bond RFQ data (wiki:
[[bergault-2023-liquidity-dynamics-rfq]]); Barzykin & Ciceri 2026 treat bond market making with a
hit-ratio target (wiki: [[barzykin-2026-bond-market-making]]).

### Foreign exchange (FX)

FX means trading one currency against another. A **currency pair** like EURUSD has a price that
says how many US dollars one euro costs (e.g. 1.0850). The most traded pairs are the "majors"
(EURUSD, GBPUSD, USDJPY). A **cross** is a pair that does not involve the dollar, such as EURGBP.
Spot FX is overwhelmingly OTC: banks quote to clients, often by RFQ or by streaming prices, and
trade among themselves on dealer-to-dealer (D2D) platforms. Price moves are often expressed in
**basis points** (bp): 1 bp = 0.01 % = 0.0001 in relative terms.

*In the wiki:* Barzykin 2026b fits Hawkes processes to three years of HSBC spot-FX RFQs in
EURUSD, GBPUSD and USDJPY (Barzykin 2026b, wiki: [[barzykin-2026-hawkes-driven-otc]], pp. 3–5).
Barzykin, Bergault & Guéant 2022 model a multi-currency dealer (wiki:
[[barzykin-2022-multi-currency-inventory]]).

### Futures

A futures contract is a standardised agreement to buy or sell an underlying (a stock index, a
bond, oil, a currency) at a fixed price on a future date. In practice almost nobody waits for the
delivery date; futures are used to take or hedge exposure cheaply. Key features:
- they trade on **exchanges** in a central limit order book;
- every trade is public and every market order has a visible **aggressor** side (Section 4);
- many contracts are tightly **related**: an equity index future and its "mini" version, or
  bond futures of neighbouring maturities. Their prices move together, and activity in one often
  spills into the other.

*Why futures matter for this project:* the Stage 2a design fixes **exchange-traded futures** as the
target market, because there all aggressor orders are public and the "flow-driven" modelling
convention (Section 3, and `E2-...`) is natural; RFQ/OTC is out of scope
(design, "Model specification (fixed)"). The wiki currently holds **no branching-ratio estimate for
futures** (design, "Relevance / State of the field"). The only futures number in the wiki is
the power-law kernel exponent $\approx0.15$ for S&P futures, cited from Hardiman–Bercot–Bouchaud by
Acero et al. 2026 (wiki: [[acero-2026-hawkes-structured-networks]], fn. 1, p. 2); that is a decay
exponent, not a branching ratio.

### Options

An option gives the right, not the obligation, to buy (call) or sell (put) an underlying at a fixed
price. Options market making is a large business but involves extra state variables (the
underlying price, volatility), so it is outside this project.

*In the wiki:* Rosenbaum & Zhang 2022 treat SPX and VIX futures and options together (wiki:
[[rosenbaum-2022-multi-asset-market]]); Lai, Gao & Li 2023 do options market making with deep
learning (wiki: [[lai-2023-data-driven-deep]]).

### What the models need from an asset

Look at what the models actually use, and you see why one framework covers all these classes:
1. a **reference price** $S^i_t$ for each asset $i$, moving randomly (Brownian motion with
   volatility $\sigma_i$; correlations collected in the covariance matrix $\Sigma$);
2. a **stream of client orders** on each side (buy and sell), arriving at random times with some
   intensity $\lambda$;
3. a **fill rule**: how likely the market maker's quote is to win an order, depending on how far
   it sits from the reference price.

The asset class decides which numbers you plug in and which convention for (2) is realistic, not
the structure of the model.

### In one breath

Stocks and futures trade on exchanges, bonds and FX mostly OTC. The project's models abstract each
asset to a random reference price, a random stream of buy and sell orders, and a fill rule. The
project's chosen target is exchange-traded futures, where all aggressor orders are visible; the
wiki's Hawkes evidence so far comes mostly from equities, FX RFQs and crypto.

---

## 3. Where it is traded: exchanges, OTC dealer markets, RFQ

### Exchanges (order-driven markets)

An exchange runs a **central limit order book** (CLOB): everyone sends orders to one electronic
book, which matches them by fixed rules (Section 4). Anyone with access can be a liquidity
provider by posting limit orders. Trades are reported publicly in real time. This is called an
**order-driven** market: prices come from the orders resting in the book.

### OTC dealer markets (quote-driven markets)

"Over the counter" means there is no central book. Clients trade bilaterally with **dealers**
(usually banks) who quote prices. This is a **quote-driven** market: prices come from dealers'
quotes. Post-trade transparency is limited; a client often does not see what other clients did.

### RFQ: request for quote

The dominant electronic OTC protocol for bonds and much of FX:
1. A client sends a **request** ("I want to buy 10 million EURUSD") to one or several dealers.
2. Each dealer answers with a price.
3. The client picks the best price (or none). The dealer who wins gets the trade.

Vocabulary:
- **Hit ratio / win ratio**: the share of requests a dealer wins. A desk tracks it as a key
  performance indicator; Barzykin & Ciceri 2026 make it an explicit control target
  (wiki: [[barzykin-2026-bond-market-making]], p. 2).
- **Fill probability / win probability** $f(\delta)$: the probability of winning as a function of
  how aggressive the quote is. In RFQ markets it is often an S-shaped (logistic) curve. In BEGV's
  example it is about 33 % at the mid and about 40 % one cent better
  (wiki: [[bergault-2021-closed-form-approximations]], p. 131).
- **Streaming (RFS)**: the dealer continuously streams executable prices instead of answering
  each request.
- **Last look**: in FX, a short check after a client hits a streamed price, letting the dealer
  reject trades at stale prices (wiki: [[barzykin-2026-strategic-otc-reputation]],
  [[barzykin-2026-dynamic-slippage-control]]). Not used in this project.

### Why the venue changes the model: who excites the flow

This is the economically important part. In a Hawkes model, each event raises the intensity of
future events. The question **which events count** depends on the venue:

- **Exchange (futures):** every market order prints publicly. Other traders see it and react.
  So it is natural to let **all** market orders excite the flow, whether or not they traded
  against our market maker. That is the **flow-driven** convention, the one the project uses.
- **OTC RFQ:** a client does not see other clients' requests. Bergault & Guéant 2023 therefore
  reject Hawkes processes for RFQ flow: «in a market with limited post-trade transparency, we
  argue that it is odd to assume that an RFQ sent by a client is the consequence of an RFQ sent by
  another client» (wiki: [[bergault-2023-liquidity-dynamics-rfq]], p. 4). They use regime-switching
  intensities instead. Barzykin 2026b nevertheless fits Hawkes to FX RFQs, and says explicitly that
  he reads the fit as **predictive, not causal** (wiki: [[barzykin-2026-hawkes-driven-otc]],
  pp. 2, 5).
- **Fill-driven** alternative: only the market maker's *own* fills excite. This is Jusselin's
  setting (one market maker who fills every order) and the Hawkes-liquidity model of Bergault et
  al. 2024 (wiki: [[who-excites-the-flow]]).

Why an economist cares: under the flow-driven convention the market maker **cannot steer** future
order flow with his quotes; it is weather, not something he causes. Under the fill-driven
convention, quoting aggressively today *creates* more flow tomorrow. Mathematically, the choice
decides which closed form survives ([[problem-anatomy]] §3; `M3-...`). Economically, it is a
question about the market: do traders react to all prints or only to particular trades? `E2-...`
develops this.

**A tension worth knowing.** BEGV note that their family of models has been «more useful to build
market making algorithms in quote-driven markets» (RFQ bonds, FX RFQ/RFS) than in order-driven
stock markets, where order-book models are used instead (wiki:
[[bergault-2021-closed-form-approximations]], p. 102). The project applies the BEGV machinery to
exchange futures. That is a legitimate modelling choice (the flow-driven convention fits exchanges
better), but it means the model ignores queue position and order-book detail (Section 4).

### In one breath

Exchanges match orders in one public book; OTC markets run through dealers, often by RFQ. Venue
matters because it decides which events plausibly trigger more events. On exchanges all prints are
public, so the project lets all market orders excite the flow (flow-driven). In RFQ markets that
assumption is contested.

---

## 4. The limit order book: bid, ask, mid, spread, tick, depth, orders, aggressor

### Intuition and a worked book

A limit order book is two queues of waiting orders: buyers who name the highest price they will pay,
and sellers who name the lowest price they will accept. Here is a small book for a stock with a
tick of 0.01:

| Bids (buyers): price | size | | Asks (sellers): price | size |
|---|---|---|---|---|
| **100.00** | 300 | | **100.02** | 200 |
| 99.99 | 500 | | 100.03 | 400 |
| 99.98 | 800 | | 100.04 | 900 |
| 99.97 | 1,200 | | 100.05 | 1,500 |

Read it like this:
- **Best bid** = 100.00: the highest price someone is currently willing to pay. If you want to
  sell immediately, this is what you get (for up to 300 shares).
- **Best ask** (or "offer") = 100.02: the lowest price someone is currently willing to sell at. If
  you want to buy immediately, you pay this.
- **Mid-price** = (100.00 + 100.02)/2 = **100.01**. The usual proxy for "fair value" now. In the
  models, the reference price $S_t$ plays this role.
- **Bid–ask spread** = 100.02 − 100.00 = **0.02** = 2 ticks. The cost of a round trip for someone
  who buys and immediately sells at market. Half of it (0.01) is the **half-spread**, the cost of
  one immediate trade relative to the mid.
- **Tick size** = 0.01: the minimum price increment. The spread can never be smaller than one tick.
- **Depth**: how much is available at or near the best prices. Here, 300 at the best bid and
  300+500+800+1,200 = 2,800 within four ticks. A deep book absorbs large orders without moving
  the price much.

### Two kinds of orders

- **Limit order**: "buy up to 500 at 99.99 or better". It rests in the book until someone trades
  against it, or until it is cancelled. Posting limit orders **provides** liquidity. The person who
  posted it is the **passive** side of any trade.
- **Market order**: "buy 500 now at whatever price". It executes immediately against resting limit
  orders, starting from the best price. It **takes** liquidity. The sender is the **aggressor**
  (or "initiator").

Worked example. A market buy order for 500 shares arrives at the book above. It takes 200 at
100.02 and the next 300 at 100.03. Average price = (200·100.02 + 300·100.03)/500 = **100.026**.
Compared with the mid of 100.01, the buyer paid 1.6 cents per share for immediacy. The best ask
is now 100.03 (100 shares left there), the new mid 100.015. The order "walked the book".

### The aggressor and trade signs

Every trade on an exchange has a passive side and an aggressor side. A trade is **buyer-initiated**
(sign +1) if the aggressor was a buyer (a market buy hit the ask), **seller-initiated** (sign −1)
if a market sell hit the bid. Exchange data usually report this directly. Order-flow models count
market orders **by aggressor side**: one counting process for aggressive buys, one for aggressive
sells, per asset. With $d$ assets that is $2d$ processes, and $2d$ intensities: this is why the
project's intensity vector is $\lambda\in\mathbb R^{2d}$ (design, "Model specification").

### Priority and queues

Most exchanges match by **price–time priority**: better prices first; at the same price, earlier
orders first. A market maker who posts at the best bid joins the **back of the queue**; he is
filled only after the 300 shares ahead of him. Queue position is a big deal in practice, and the
reason why speed matters.

*What the project's models do with this:* they ignore queues. They summarise the whole
"probability of being filled" story by one function of the distance from the mid (next
subsection). GLFT say plainly that their model is continuous while the real problem is discrete
because of the tick size, and that quotes must be rounded to the tick in practice (wiki:
[[gueant-2013-dealing-inventory-risk]], §7, p. 493).

### The market maker's quotes: $\delta^b$ and $\delta^a$

In the models, the market maker posts one bid and one ask around the reference price $S_t$:

$$\text{bid} = S_t-\delta^b_t,\qquad \text{ask}=S_t+\delta^a_t .$$

$\delta^b$ and $\delta^a$ are **distances from the mid**, in price units (ticks, cents, bp). They are
the control variables: the only thing the market maker chooses.

Worked example: $S_t=100.01$, $\delta^b=0.02$, $\delta^a=0.03$ → bid 99.99, ask 100.04. The quoted
spread is $\delta^b+\delta^a=0.05$.

**Which orders fill which side.** A client's *market sell* order can hit the maker's **bid**: the
maker buys, his inventory goes **up** by one. A client's *market buy* order can lift the maker's
**ask**: the maker sells, inventory goes **down**. Keep this straight; it is easy to flip.

### The fill probability $f(\delta)$ and intensity $\Lambda e^{-k\delta}$

The further from the mid you quote, the less likely an arriving market order reaches you (it would
have to be large, or the price would have to move to you). The standard model since
Avellaneda–Stoikov: market orders that could reach the maker arrive at some rate; a quote at
distance $\delta$ is filled at rate

$$\Lambda e^{-k\delta}.$$

- $\Lambda$ (Lambda): the fill rate if you quote **at** the mid ($\delta=0$), in orders per unit
  time.
- $k$: how fast the fill rate drops as you move away, per unit of price.

Equivalently, the project writes the fill probability per arriving order as $f(\delta)=\Lambda
e^{-k\delta}$ "per unit intensity" (design, "Model specification"), so that the fill rate on side
$j$ is $\lambda_j f(\delta)$: arrivals times probability of winning. With Hawkes flow the
arrival rate $\lambda_j$ is random and moves; with Poisson flow it is constant.

Worked example with the GLFT benchmark values $\Lambda=0.9$ per second and $k=0.3$ per tick
(wiki: [[glft-2013-model]], parameters confirmed against Figs. 1–3, pp. 483–484):

| Distance $\delta$ (ticks) | Fill rate $0.9e^{-0.3\delta}$ (per second) | Expected seconds between fills |
|---|---|---|
| 0 | 0.900 | 1.1 |
| 1 | 0.667 | 1.5 |
| 3 | 0.366 | 2.7 |
| 5 | 0.201 | 5.0 |
| 10 | 0.045 | 22.3 |

(my arithmetic; seconds between fills = 1/rate.) Every tick further out costs about 26 % of fills
($e^{-0.3}\approx0.74$).

In RFQ markets the analogous object is the S-shaped win probability, e.g. BEGV's logistic curve
$1/(1+e^{\alpha+\beta\delta})$ (wiki: [[bergault-2021-closed-form-approximations]], p. 131), and
Barzykin's sigmoid (wiki: [[barzykin-2026-hawkes-driven-otc]], p. 6).

### Why it matters here

The exponential fill curve is not just convenient; it is what makes GLFT's exact closed form work
([[problem-anatomy]] §1a). And the project's three economic ingredients appear right here: the
reference price $S_t$ (price risk), the order arrivals $\lambda$ (how much business), and the fill
curve $f(\delta)$ (the trade-off between price and probability).

### In one breath

The book shows the best bid, best ask, their mid and spread, and the depth behind them. Limit orders
wait and provide liquidity; market orders execute now and take it, and their sender is the
aggressor. The models replace queues by a fill rate $\Lambda e^{-k\delta}$ that falls exponentially
with the quote's distance $\delta$ from the mid; the maker chooses $\delta^b$ and $\delta^a$.

---

## 5. Market makers: who they are and how they earn

### Who they are

- **Designated market makers** on exchanges: firms that sign an agreement with the exchange to
  keep quotes on both sides for a share of the trading day, within a maximum spread, in return for
  fee discounts (general knowledge; Section 14).
- **Electronic / high-frequency trading firms** that provide liquidity by algorithm across many
  instruments, without a formal designation.
- **Bank dealers** in OTC markets (FX, bonds, rates), who answer client RFQs and stream prices.
  Barzykin's papers come from a bank FX desk (the data are «anonymised HSBC spot-FX RFQs», wiki:
  [[barzykin-2026-hawkes-driven-otc]], p. 3). GLFT note that «adaptations of our results are in use
  at Cheuvreux», a broker (wiki: [[gueant-2013-dealing-inventory-risk]], p. 479).

### How they earn: the spread

The core business is to buy at the bid and sell at the ask. If a client sells to you at 99.99 and
a few seconds later another client buys from you at 100.03, you earned 0.04 on that **round trip**,
without any view on where the price is going. This is **spread capture**.

Worked example: one round trip per 10 seconds, 100 shares each, 4 cents captured per share. Per
hour: 360 round trips × 100 × 0.04 = **1,440** in currency units. Small per trade, large in
aggregate, *provided* the price does not move against you in between. Section 6 is about that
proviso.

### How they earn: rebates

Many exchanges use **maker–taker** pricing: the aggressor (taker) pays a fee per share, and part of
it goes to the passive side (maker) as a **rebate**. For a market maker trading millions of shares,
rebates can be a significant part of revenue. The project's models do not include fees or rebates;
one could add a constant per-fill rebate to $\delta$ without changing the structure (my remark, not
from a source). BEGV note that proportional costs can be handled by shifting the intensity
(wiki: [[bergault-2021-closed-form-approximations]], note 16).

### The basic trade-off: price versus probability

Quote close to the mid and you are filled often but earn little per fill. Quote far and you earn a
lot per fill but rarely trade. Ignore risk for a moment. The expected earning rate on one side is

$$\underbrace{\delta}_{\text{earned per fill}}\times\underbrace{\Lambda e^{-k\delta}}_{\text{fills per second}} .$$

Worked example ($\Lambda=0.9$, $k=0.3$):

| $\delta$ (ticks) | earning rate $\delta\cdot0.9e^{-0.3\delta}$ (ticks per second) |
|---|---|
| 1 | 0.667 |
| 2 | 0.988 |
| 3 | 1.098 |
| **3.33** | **1.104** |
| 4 | 1.084 |
| 6 | 0.893 |

(my arithmetic.) The best distance is $\delta=1/k=3.33$ ticks. In general, maximising
$\delta e^{-k\delta}$ gives $1/k$: the derivative $e^{-k\delta}(1-k\delta)$ vanishes at $\delta=1/k$.
This is the **risk-neutral quote**. It reappears in the papers: BEGV's Model B quotes contain
exactly a term $+1/k$ (wiki: [[bergault-2021-closed-form-approximations]], p. 118), and CJR call
the analogous term the «risk-neutral» part of the quote, which maximises $\delta h(\delta)$
(wiki: [[cartea-2014-buy-low-sell]], p. 428).

Notice what $k$ means economically. A large $k$ means fills die off fast with distance: competition
is fierce, the book is deep near the mid, and you must quote tight. GLFT find exactly this: a larger
$k$ narrows the optimal spread (wiki: [[gueant-2013-dealing-inventory-risk]], §6.5, p. 492).

### In one breath

Market makers are exchange-designated firms, electronic liquidity providers and bank dealers. They
earn the spread on round trips, plus rebates on some exchanges. Each quote trades price against
probability; without risk the best distance under an exponential fill curve is $1/k$, the
risk-neutral quote.

---

## 6. Inventory, inventory risk and quote skew

### Intuition

Round trips do not come in neat pairs. Three clients in a row may sell to you. Now you hold 3 units
you did not plan to hold: your **inventory** is $q=+3$. While you hold them, the price can fall.
That is **inventory risk**: the risk of losing money on positions you were forced to take by the
order flow, while waiting to offload them.

Inventory risk is what turns a simple pricing problem into a control problem. Without it, you would
just quote $1/k$ on each side forever.

### The state variables

- $q_t$: inventory (number of units held; negative means **short**, you sold units you did not have
  and owe them).
- $X_t$: cash.
- $S_t$: reference (mid) price.
- $Q$: an inventory bound. Most models impose $|q|\le Q$ as a **risk limit**: at $q=Q$ the maker
  stops buying (no bid), at $q=-Q$ he stops selling. GLFT call this «a realistic restriction [that]
  may be read as a risk limit» and use it to make the problem rigorously solvable (wiki:
  [[gueant-2013-dealing-inventory-risk]], p. 480). The plan fixes $Q=5$ (plan, "Core parameters").

### How big is inventory risk? A worked example

The models let the price move like a Brownian motion: over a time $\Delta t$ the change in $S$ is
random with mean 0 and standard deviation $\sigma\sqrt{\Delta t}$ (`M1-...` explains why the square
root). With GLFT's $\sigma=0.3$ tick per $\sqrt{\text{second}}$:
- over 1 second: standard deviation 0.3 ticks;
- over 60 seconds: $0.3\sqrt{60}\approx$ **2.3 ticks**.

Holding $q=5$ units for a minute, the value of the position changes by $5\times\Delta S$, with
standard deviation $5\times2.3\approx$ **11.6 ticks**. Compare with the spread income: at about 3.3
ticks per fill, that minute of risk is worth the margin on 3–4 fills. Inventory risk grows like
$q^2$ in variance: twice the inventory, four times the variance. That is why the penalty in the
objective is **quadratic** in $q$ (Section 11).

### Skew: how a market maker manages inventory with prices

A market maker who is long wants to **sell** more and **buy** less. He cannot order clients to
trade, but he can change prices:
- move the **ask closer** to the mid (smaller $\delta^a$): more clients buy from him, inventory falls;
- move the **bid further** away (larger $\delta^b$): fewer clients sell to him.

Both quotes shift **down** together. This is **skewing** the quotes. A short market maker shifts
both up. The **spread** $\delta^b+\delta^a$ may stay almost constant while the **skew**
$\tfrac12(\delta^a-\delta^b)$ moves with inventory.

Worked example. Flat ($q=0$): mid 100.00, quotes 99.97 / 100.03, symmetric. Long $q=+4$: the maker
shifts both quotes down by 1 tick: 99.96 / 100.02. The spread is still 6 ticks; the ask is now 2
ticks from the mid instead of 3, so (using the table in Section 4, ratio $e^{0.3}$) buyers fill him
about 35 % more often, while sellers fill him about 26 % less often. Inventory drifts back to 0.

A useful way to say the same: the long maker behaves as if the price were lower than the mid. The
point around which he quotes symmetrically, here 99.99, is his **reservation price** (an
Avellaneda–Stoikov idea; see `M2-...`). Inventory pulls the reservation price away from the mid.

### What the closed forms actually say: a numerical example

GLFT's asymptotic closed-form quotes (CARA objective) for one asset are approximately
(wiki: [[gueant-2013-dealing-inventory-risk]], p. 485):

$$\delta^{b}\approx\tfrac1\gamma\ln\!\big(1+\tfrac\gamma k\big)+\tfrac{2q+1}{2}\,c,\qquad
\delta^{a}\approx\tfrac1\gamma\ln\!\big(1+\tfrac\gamma k\big)+\tfrac{1-2q}{2}\,c,\qquad
c=\sqrt{\tfrac{\sigma^2\gamma}{2k\Lambda}\big(1+\tfrac\gamma k\big)^{1+k/\gamma}} .$$

(GLFT write $A$ for $\Lambda$; the project reserves $A$ for the Riccati matrix.) Plug in the
benchmark $\sigma=0.3$, $\Lambda=0.9$, $k=0.3$, $\gamma=0.01$ (my arithmetic):
- static part $\tfrac1\gamma\ln(1+\gamma/k)=100\ln(1.0333)\approx3.279$ ticks, close to the
  risk-neutral $1/k=3.333$;
- skew coefficient $c\approx0.068$ ticks per unit of inventory;
- at $q=0$: spread $\approx2\times3.279+0.068=6.626$ ticks. This matches the 6.626 ticks the wiki
  reports from a full reproduction at $q=0$ (wiki: [[glft-2013-model]], "Contested / inference").
- at $q=+10$: the bid moves out by $10c\approx0.68$ ticks, the ask moves in by the same. Spread
  unchanged; the whole quote pair shifts down.

The BEGV formulas say the same in matrix form (risk-adjusted objective, Model B): half-spread
$\tfrac12\sqrt\gamma\,z\,e^{i\top}\Gamma e^i+\tfrac1k$ and skew $-\sqrt\gamma\,q^\top\Gamma e^i$
(wiki: [[bergault-2021-closed-form-approximations]], p. 119). BEGV's reading: «the skew has the role
of inventory risk management, whereas the spread balances the trade-off between frequency of
transactions and profit per round-trip trade» (p. 119). For one asset with the GLFT numbers,
$\Gamma=\sigma/\sqrt{D_+}$ with $D_+=2\Lambda e^{-1}k\approx0.199$ gives $\Gamma\approx0.673$ and a
skew coefficient $\sqrt\gamma\Gamma\approx0.067$ ticks per unit, practically the GLFT value (my
arithmetic from the p. 118 formulas). Two different routes, the same economics.

### Comparative statics: what moves the quotes

GLFT report how the quotes respond to each parameter (wiki: [[gueant-2013-dealing-inventory-risk]],
§6, pp. 489–492):
- **Higher volatility $\sigma$** → wider spread, steeper skew: «an increase in $\sigma^2$ increases
  inventory risk» (p. 490).
- **More order flow $\Lambda$** → the opposite of volatility: more trades mean «the risk of being
  stuck with a large inventory» falls (p. 490). In the closed form $\sigma^2$ and $\Lambda$ enter the
  inventory term only through $\sigma^2/\Lambda$.
- **Larger $k$** → narrower spread (Section 5).
- **Risk aversion $\gamma$** → ambiguous (Section 10).

The second bullet is **the economic heart of this project**. If order flow arrives in bursts, the
amount of flow expected in the next minutes is not constant. During a burst the market maker
expects many trades, so inventory is easy to offload, so he needs less skew and can take on
inventory more freely. In a lull, the reverse. A model with constant $\Lambda$ cannot see this; a
Hawkes model can. Barzykin 2026b finds that conditioning on the burst «primarily improves
inventory-risk control» (wiki: [[barzykin-2026-hawkes-driven-otc]], p. 20).

### The shadow price of inventory

How much does one more unit of inventory cost the market maker, in value terms? That number is the
**shadow price** $p$ (wiki: [[shadow-price]]). Economically: if taking one more unit makes your
future worse by $p$ (because of the extra risk and the cost of offloading it), you should demand at
least $p$ of compensation, on top of the normal margin, before buying it. In the risk-adjusted model
with exponential fills the optimal quote is literally

$$\delta^*=p+\tfrac1k$$

(BEGV Model B, $\tilde\delta^*(p)=p+1/k$, wiki: [[bergault-2021-closed-form-approximations]],
p. 118): the shadow price plus the risk-neutral margin. Long inventory makes buying more costly
(positive $p$ on the bid) and selling attractive (negative $p$ on the ask); that is the skew again.

Under Hawkes flow the shadow price is evaluated at the intensities **just after** the order arrives,
because the arriving order itself changes the forecast of future flow (wiki: [[shadow-price]];
proposal p. 19). Barzykin splits it into an inventory term and an «information value» term: the
channel through which a burst skews quotes (wiki: [[barzykin-2026-hawkes-driven-otc]], eq. (43),
p. 12). The mathematics is in `M2-...` and `M3-...`.

### In one breath

Inventory $q$ is the position forced on the maker by the flow; its price risk grows like $q^2$.
The maker controls it by skewing both quotes in the same direction, keeping the spread roughly
fixed. More expected flow means inventory is easier to offload and calls for less skew; Hawkes
bursts make that expected flow move over time. The shadow price $p$ is the value cost of one more
unit, and the optimal quote is $p$ plus the risk-neutral margin.

---
