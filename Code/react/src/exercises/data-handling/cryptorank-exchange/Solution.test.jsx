import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import CryptoRankExchange from "./Solution.jsx";

const type = (value) => fireEvent.change(screen.getByPlaceholderText("USD"), { target: { value } });
const coins = (code) => screen.getByTestId(`coins-${code}`);

describe("CryptoRank Exchange", () => {
  it("starts with 0.00000000 coins and no error", () => {
    render(<CryptoRankExchange />);
    expect(screen.getByText("of my $17042.67:")).toBeInTheDocument();
    expect(coins("BTC")).toHaveTextContent("0.00000000");
    expect(screen.queryByTestId("error")).not.toBeInTheDocument();
  });

  it("converts a valid amount with 8 decimals", () => {
    render(<CryptoRankExchange />);
    type("100");
    expect(coins("BNB")).toHaveTextContent("0.31183900");
    expect(coins("DOGE")).toHaveTextContent("1118.55872200");
    expect(coins("XRP")).toHaveTextContent("250.68263400");
    expect(screen.queryByTestId("error")).not.toBeInTheDocument();
  });

  it("shows the right error messages", () => {
    render(<CryptoRankExchange />);
    type("0");
    expect(screen.getByTestId("error")).toHaveTextContent("Amount cannot be less than $0.01");
    expect(coins("BTC")).toHaveTextContent("n/a");

    type("20000");
    expect(screen.getByTestId("error")).toHaveTextContent("Amount cannot exceed the available balance");
    expect(coins("ETH")).toHaveTextContent("n/a");

    type("");
    expect(screen.getByTestId("error")).toHaveTextContent("Amount cannot be empty");
    expect(coins("ETH")).toHaveTextContent("0.00000000");
  });

  it("accepts the full balance and the minimum", () => {
    render(<CryptoRankExchange />);
    type("17042.67");
    expect(screen.queryByTestId("error")).not.toBeInTheDocument();
    type("0.01");
    expect(screen.queryByTestId("error")).not.toBeInTheDocument();
  });
});
