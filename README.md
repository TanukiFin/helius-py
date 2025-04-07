
# Enhanced Transactions API
https://docs.helius.dev/solana-apis/enhanced-transactions-api


| url  | input  | input type| output  |
|--|--|--|--|
|https://api.helius.xyz/v0/transactions | signatures | list | [] |
|https://api.helius.xyz/v0/addresses/{address}/transactions  | address | str | [] |
```python
import requests

api_key = "your_api_key_here"
url = f"https://api.helius.xyz/v0/transactions/?api-key={api_key}"

param = {
    "transactions": [
        "593wEz7afr4bH8puUEeqVeDsFAcWSnwydmU4NkHDFX19Hdvf2i5tJF6WheU6RRd6F7jHgUh6kEvujiUPCo36x8Do",
        "4DCrERdsW3q6QZtaswEw4Ut9qDWLFKixUxmZUvLvSYC3mxVk4eSBk2RLHXcTC6TkFb93eycvPiTeWC71kFFQiyj9"
    ]
}

response = requests.get(url, params=params)
data = response.json()
```

<details>
<summary>Return</summary>

```python
[
  {
    "description": "Human readable interpretation of the transaction",
    "type": "UNKNOWN",
    "source": "FORM_FUNCTION",
    "fee": 5000,
    "feePayer": "8cRrU1NzNpjL3k2BwjW3VixAcX6VFc29KHr4KZg8cs2Y",
    "signature": "yy5BT9benHhx8fGCvhcAfTtLEHAtRJ3hRTzVL16bdrTCWm63t2vapfrZQZLJC3RcuagekaXjSs2zUGQvbcto8DK",
    "slot": 148277128,
    "timestamp": 1656442333,
    "nativeTransfers": [
      {
        "fromUserAccount": "text",
        "toUserAccount": "text",
        "amount": 1
      }
    ],
    "tokenTransfers": [
      {
        "fromUserAccount": "text",
        "toUserAccount": "text",
        "fromTokenAccount": "text",
        "toTokenAccount": "text",
        "tokenAmount": 1,
        "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx"
      }
    ],
    "accountData": [
      {
        "account": "text",
        "nativeBalanceChange": 1,
        "tokenBalanceChanges": [
          {
            "userAccount": "F54ZGuxyb2gA7vRjzWKLWEMQqCfJxDY1whtqtjdq4CJ",
            "tokenAccount": "2kvmbRybhrcptDnwyNv6oiFGFEnRVv7MvVyqsxkirgdn",
            "mint": "DUSTawucrTsGU8hcqRdHDCbuYhCPADMLM2VcCb8VnFnQ",
            "rawTokenAmount": {
              "tokenAmount": "text",
              "decimals": 1
            }
          }
        ]
      }
    ],
    "transactionError": {
      "error": "text"
    },
    "instructions": [
      {
        "accounts": [
          "8uX6yiUuH4UjUb1gMGJAdkXorSuKshqsFGDCFShcK88B"
        ],
        "data": "kdL8HQJrbbvQRGXmoadaja1Qvs",
        "programId": "MEisE1HzehtrDpAAT8PnLHjpSSkRYakotTuJRPjTpo8",
        "innerInstructions": [
          {
            "accounts": [
              "text"
            ],
            "data": "text",
            "programId": "text"
          }
        ]
      }
    ],
    "events": {
      "nft": {
        "description": "text",
        "type": "NFT_BID",
        "source": "FORM_FUNCTION",
        "amount": 1000000,
        "fee": 5000,
        "feePayer": "8cRrU1NzNpjL3k2BwjW3VixAcX6VFc29KHr4KZg8cs2Y",
        "signature": "4jzQxVTaJ4Fe4Fct9y1aaT9hmVyEjpCqE2bL8JMnuLZbzHZwaL4kZZvNEZ6bEj6fGmiAdCPjmNQHCf8v994PAgDf",
        "slot": 148277128,
        "timestamp": 1656442333,
        "saleType": "AUCTION",
        "buyer": "text",
        "seller": "text",
        "staker": "text",
        "nfts": [
          {
            "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx",
            "tokenStandard": "NonFungible"
          }
        ]
      },
      "swap": {
        "nativeInput": {
          "account": "2uySTNgvGT2kwqpfgLiSgeBLR3wQyye1i1A2iQWoPiFr",
          "amount": "100000000"
        },
        "nativeOutput": {
          "account": "2uySTNgvGT2kwqpfgLiSgeBLR3wQyye1i1A2iQWoPiFr",
          "amount": "100000000"
        },
        "tokenInputs": [
          {
            "userAccount": "F54ZGuxyb2gA7vRjzWKLWEMQqCfJxDY1whtqtjdq4CJ",
            "tokenAccount": "2kvmbRybhrcptDnwyNv6oiFGFEnRVv7MvVyqsxkirgdn",
            "mint": "DUSTawucrTsGU8hcqRdHDCbuYhCPADMLM2VcCb8VnFnQ",
            "rawTokenAmount": {
              "tokenAmount": "text",
              "decimals": 1
            }
          }
        ],
        "tokenOutputs": [
          {
            "userAccount": "F54ZGuxyb2gA7vRjzWKLWEMQqCfJxDY1whtqtjdq4CJ",
            "tokenAccount": "2kvmbRybhrcptDnwyNv6oiFGFEnRVv7MvVyqsxkirgdn",
            "mint": "DUSTawucrTsGU8hcqRdHDCbuYhCPADMLM2VcCb8VnFnQ",
            "rawTokenAmount": {
              "tokenAmount": "text",
              "decimals": 1
            }
          }
        ],
        "tokenFees": [
          {
            "userAccount": "F54ZGuxyb2gA7vRjzWKLWEMQqCfJxDY1whtqtjdq4CJ",
            "tokenAccount": "2kvmbRybhrcptDnwyNv6oiFGFEnRVv7MvVyqsxkirgdn",
            "mint": "DUSTawucrTsGU8hcqRdHDCbuYhCPADMLM2VcCb8VnFnQ",
            "rawTokenAmount": {
              "tokenAmount": "text",
              "decimals": 1
            }
          }
        ],
        "nativeFees": [
          {
            "account": "2uySTNgvGT2kwqpfgLiSgeBLR3wQyye1i1A2iQWoPiFr",
            "amount": "100000000"
          }
        ],
        "innerSwaps": [
          {
            "tokenInputs": [
              {
                "fromUserAccount": "text",
                "toUserAccount": "text",
                "fromTokenAccount": "text",
                "toTokenAccount": "text",
                "tokenAmount": 1,
                "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx"
              }
            ],
            "tokenOutputs": [
              {
                "fromUserAccount": "text",
                "toUserAccount": "text",
                "fromTokenAccount": "text",
                "toTokenAccount": "text",
                "tokenAmount": 1,
                "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx"
              }
            ],
            "tokenFees": [
              {
                "fromUserAccount": "text",
                "toUserAccount": "text",
                "fromTokenAccount": "text",
                "toTokenAccount": "text",
                "tokenAmount": 1,
                "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx"
              }
            ],
            "nativeFees": [
              {
                "fromUserAccount": "text",
                "toUserAccount": "text",
                "amount": 1
              }
            ],
            "programInfo": {
              "source": "ORCA",
              "account": "whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc",
              "programName": "ORCA_WHIRLPOOLS",
              "instructionName": "whirlpoolSwap"
            }
          }
        ]
      },
      "compressed": {
        "type": "COMPRESSED_NFT_MINT",
        "treeId": "text",
        "assetId": "text",
        "leafIndex": 1,
        "instructionIndex": 1,
        "innerInstructionIndex": 1,
        "newLeafOwner": "text",
        "oldLeafOwner": "text"
      },
      "distributeCompressionRewards": {
        "amount": 1
      },
      "setAuthority": {
        "account": "text",
        "from": "text",
        "to": "text",
        "instructionIndex": 1,
        "innerInstructionIndex": 1
      }
    }
  }
]
```

</details>

<br><br>


```python
import requests

api_key = "your_api_key_here"
address = "your_address_here"

url = f"https://api.helius.xyz/v0/addresses/{address}/transactions?api-key={api_key}"

params = {
            "before": "your_signature_here", # 在這之前
            "after": "your_signature_here", # 在這之後
        }

response = requests.get(url, params=params )
data = response.json()
```

<br><br>

# Digital Asset Standard (DAS) API
https://docs.helius.dev/compression-and-das-api/digital-asset-standard-das-api

| 功能名稱                    | 說明                                                               | API 方法名稱               |
|---------------------------|--------------------------------------------------------------------|----------------------------|
| Get Asset                 | 根據資產 ID 取得單一資產資訊。                                    | `getAsset`                 |
| Get Asset Batch           | 根據多個資產 ID 一次取得多個資產資訊。                            | `getAssetBatch`           |
| Get Asset Proof           | 根據資產 ID 取得壓縮資產的 Merkle 證明。                          | `getAssetProof`           |
| Get Asset Proof Batch     | 根據多個資產 ID 一次取得多個 Merkle 證明。                        | `getAssetProofBatch`      |
| Search Assets             | 使用多種參數搜尋資產。                                            | `searchAssets`            |
| Get Assets by Owner       | 根據地址取得該地址擁有的資產清單。                                | `getAssetsByOwner`        |
| Get Assets by Authority   | 根據特定 authority 取得其相關資產清單。                           | `getAssetsByAuthority`    |
| Get Assets by Creator     | 根據創建者地址取得其創建的資產清單。                              | `getAssetsByCreator`      |
| Get Assets by Group       | 根據群組鍵與值取得資產清單。                                      | `getAssetsByGroup`        |
| Get Signatures For Asset  | 取得與壓縮資產相關的交易簽章紀錄。                                | `getSignaturesForAsset`   |
| Get Token Accounts        | 取得特定 mint 或 owner 所有的 token 帳戶資訊。                    | `getTokenAccounts`        |
| Get Nft Editions          | 取得特定主 NFT 的所有 edition NFTs 資訊。                        | `getNftEditions`          |


# HTTP
Solana 節點使用 JSON-RPC 2.0 規格接受 HTTP 請求。